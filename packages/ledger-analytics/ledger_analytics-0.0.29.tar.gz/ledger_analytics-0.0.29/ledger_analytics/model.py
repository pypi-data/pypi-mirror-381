from __future__ import annotations

import time

from requests import Response
from requests.exceptions import HTTPError

from .autofit import AutofitControl
from .config import JSONDict
from .console import RichConsole
from .interface import ModelInterface, TriangleInterface
from .requester import Requester
from .triangle import Triangle


class LedgerModel(ModelInterface):
    def __init__(
        self,
        id: str,
        name: str,
        model_type: str,
        config: JSONDict | None,
        model_class: str,
        endpoint: str,
        requester: Requester,
        asynchronous: bool = False,
    ) -> None:
        super().__init__(model_class, endpoint, requester, asynchronous)

        self._endpoint = endpoint
        self._id = id
        self._name = name
        self._model_type = model_type
        self._config = config
        self._model_class = model_class
        self._fit_response: Response | None = None
        self._predict_response: Response | None = None
        self._get_response: Response | None = None
        self._captured_stdout: str = ""

    id = property(lambda self: self._id)
    name = property(lambda self: self._name)
    model_type = property(lambda self: self._model_type)
    config = property(lambda self: self._config)
    model_class = property(lambda self: self._model_class)
    endpoint = property(lambda self: self._endpoint)
    fit_response = property(lambda self: self._fit_response)
    predict_response = property(lambda self: self._predict_response)
    get_response = property(lambda self: self._get_response)
    delete_response = property(lambda self: self._delete_response)
    captured_stdout = property(lambda self: self._captured_stdout)

    @classmethod
    def get(
        cls,
        id: str,
        name: str,
        model_type: str,
        config: JSONDict,
        model_class: str,
        endpoint: str,
        requester: Requester,
        asynchronous: bool = False,
    ) -> LedgerModel:
        console = RichConsole()
        with console.status("Retrieving...", spinner="bouncingBar") as _:
            console.log(f"Getting model '{name}' with ID '{id}'")
            get_response = requester.get(endpoint, stream=True)

        self = cls(
            id,
            name,
            model_type,
            config,
            model_class,
            endpoint,
            requester,
            asynchronous,
        )
        self._get_response = get_response
        self._captured_stdout += console.get_stdout()
        return self

    @classmethod
    def fit_from_interface(
        cls,
        triangle_name: str,
        name: str,
        model_type: str,
        config: JSONDict | None,
        model_class: str,
        endpoint: str,
        requester: Requester,
        overwrite: bool = False,
        asynchronous: bool = False,
        timeout: int = 300,
    ) -> LedgerModel:
        """This method fits a new model and constructs a LedgerModel instance.
        It's intended to be used from the `ModelInterface` class mainly,
        and in the future will likely be superseded by having separate
        `create` and `fit` API endpoints.
        """

        config = config or {}

        if "autofit_override" in config:
            autofit = config["autofit_override"] or {}
            config["autofit_override"] = AutofitControl(**autofit).__dict__

        config = {
            "triangle_name": triangle_name,
            "model_name": name,
            "overwrite": overwrite,
            "model_type": model_type,
            "model_config": cls.Config(**config).__dict__,
        }
        fit_response = requester.post(endpoint, data=config)
        id = fit_response.json()["model"]["id"]
        self = cls(
            id=id,
            name=name,
            model_type=model_type,
            config=config,
            model_class=model_class,
            endpoint=endpoint + f"/{id}",
            requester=requester,
            asynchronous=asynchronous,
        )

        self._fit_response = fit_response

        if asynchronous:
            return self

        task_id = self.fit_response.json()["modal_task"]["id"]
        task_response = self._poll_remote_task(
            task_id,
            task_name=f"Fitting model '{self.name}' on triangle '{triangle_name}'",
            timeout=timeout,
        )
        if task_response.get("status") != "success":
            raise ValueError(f"Task failed: {task_response['error']}")
        return self

    def predict(
        self,
        triangle: str | Triangle,
        config: JSONDict | None = None,
        target_triangle: Triangle | str | None = None,
        prediction_name: str | None = None,
        timeout: int = 300,
        overwrite: bool = False,
    ) -> Triangle:
        triangle_name = triangle if isinstance(triangle, str) else triangle.name
        config = {
            "triangle_name": triangle_name,
            "predict_config": self.PredictConfig(**(config or {})).__dict__,
            "overwrite": overwrite,
        }
        if prediction_name:
            config["prediction_name"] = prediction_name

        if isinstance(target_triangle, Triangle):
            config["predict_config"]["target_triangle"] = target_triangle.name
        elif isinstance(target_triangle, str):
            config["predict_config"]["target_triangle"] = target_triangle

        url = self.endpoint + "/predict"
        self._predict_response = self._requester.post(url, data=config)

        if self._asynchronous:
            return self

        task_id = self.predict_response.json()["modal_task"]["id"]
        task_response = self._poll_remote_task(
            task_id=task_id,
            task_name=f"Predicting from model '{self.name}' on triangle '{triangle_name}'",
            timeout=timeout,
        )
        if task_response.get("status") != "success":
            raise ValueError(f"Task failed: {task_response['error']}")
        triangle_id = self.predict_response.json()["predictions"]
        triangle = TriangleInterface(
            host=self.endpoint.replace(f"{self.model_class_slug}/{self.id}", ""),
            requester=self._requester,
        ).get(id=triangle_id)
        return triangle

    def delete(self) -> LedgerModel:
        self._delete_response = self._requester.delete(self.endpoint)
        return self

    def terminate(self) -> LedgerModel:
        status = self.poll().get("status")

        if status is None or status.lower() not in ["created", "pending"]:
            return self

        console = RichConsole()
        timeout = 60
        start = time.time()
        with console.status("Terminating...", spinner="bouncingBar") as _:
            console.log(f"Terminating model {self.name} with ID {self.id}.")
            while status.lower() != "terminated" and time.time() - start < timeout:
                try:
                    self._requester.post(self.endpoint + "/terminate", data={})
                    status = self.poll().get("status")
                except HTTPError:
                    continue
                if status.lower() == "terminated":
                    self._captured_stdout += console.get_stdout()
                    return self
            raise TimeoutError(f"Could not terminate within {timeout} seconds.")

    def poll(self):
        try:
            task_id = self._fit_response.json()["modal_task"]["id"]
            return self._poll(task_id).json()
        except AttributeError:
            return {}

    def _poll(self, task_id: str) -> JSONDict:
        endpoint = self.endpoint.replace(
            f"{self.model_class_slug}/{self.id}", f"tasks/{task_id}"
        )
        return self._requester.get(endpoint)

    def _poll_remote_task(
        self, task_id: str, task_name: str = "", timeout: int = 300
    ) -> dict:
        start = time.time()
        status = ["CREATED"]
        console = RichConsole()
        with console.status("Working...", spinner="bouncingBar") as _:
            while time.time() - start < timeout:
                task = self._poll(task_id).json()
                modal_status = (
                    "FINISHED" if task["task_response"] is not None else "PENDING"
                )
                status.append(modal_status)
                if status[-1] != status[-2]:
                    console.log(f"{task_name}: {status[-1]}")
                if status[-1].lower() == "finished":
                    self._captured_stdout += console.get_stdout()
                    return task["task_response"]
            raise TimeoutError(f"Task '{task}' timed out")


class DevelopmentModel(LedgerModel):
    pass


class TailModel(LedgerModel):
    pass


class ForecastModel(LedgerModel):
    pass
