######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.18.10                                                                                #
# Generated on 2025-10-02T16:05:06.651998                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from ...exception import MetaflowException as MetaflowException
from .kubernetes_job import KubernetesJob as KubernetesJob
from .kubernetes_jobsets import KubernetesJobSet as KubernetesJobSet

KUBERNETES_NAMESPACE: str

CLIENT_REFRESH_INTERVAL_SECONDS: int

class KubernetesClientException(metaflow.exception.MetaflowException, metaclass=type):
    ...

class KubernetesClient(object, metaclass=type):
    def __init__(self):
        ...
    def get(self):
        ...
    def list(self, flow_name, run_id, user):
        ...
    def kill_pods(self, flow_name, run_id, user, echo):
        ...
    def jobset(self, **kwargs):
        ...
    def job(self, **kwargs):
        ...
    ...

