######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.18.10                                                                                #
# Generated on 2025-10-02T16:05:06.666594                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.decorators

from ...exception import MetaflowException as MetaflowException

class ExitHookDecorator(metaflow.decorators.FlowDecorator, metaclass=type):
    def flow_init(self, flow, graph, environment, flow_datastore, metadata, logger, echo, options):
        ...
    ...

