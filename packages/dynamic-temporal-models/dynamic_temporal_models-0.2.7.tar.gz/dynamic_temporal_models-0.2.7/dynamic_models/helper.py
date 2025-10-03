from datetime import timedelta
from temporalio import workflow
import dynamic_models.workflow_input as input_module
import temporalio.common as temporalio_common


def to_temporal_retry_policy(rp: input_module.RetryPolicy | None) -> temporalio_common.RetryPolicy | None:
    if rp is None or isinstance(rp, temporalio_common.RetryPolicy):
        return rp
    return temporalio_common.RetryPolicy(
        initial_interval=timedelta(milliseconds=rp.initial_interval) if rp.initial_interval else None,
        maximum_interval=timedelta(milliseconds=rp.maximum_interval) if rp.maximum_interval else None,
        backoff_coefficient=rp.backoff_coefficient,
        maximum_attempts=rp.maximum_attempts,
        non_retryable_error_types=rp.non_retryable_error_types,

    )


def to_timedelta(ms: int | None) -> timedelta | None:
    if ms is None:
        return None
    return timedelta(milliseconds=ms)


async def process_executor(executor: input_module.Executor, input_data: dict):
    if executor.is_workflow and executor.workflow:
        workflow_executor = workflow.execute_child_workflow if executor.wait_execution else workflow.start_child_workflow
        child_workflow = await workflow_executor(
            executor.workflow.name,
            input_module.ActivityInput(input=input_data, app_config=executor.workflow.app_config),
            id=executor.workflow.id or None,
            task_queue=executor.workflow.queue,
            retry_policy=to_temporal_retry_policy(executor.workflow.retry_policy),
            execution_timeout=to_timedelta(executor.workflow.execution_timeout),
            run_timeout=to_timedelta(executor.workflow.run_timeout),
            task_timeout=to_timedelta(executor.workflow.task_timeout),
            result_type=dict,
        )
        return child_workflow
    elif not executor.is_workflow and executor.activity:
        activity_executor = workflow.execute_activity if executor.wait_execution else workflow.start_activity
        result = await activity_executor(
            executor.activity.name,
            input_module.ActivityInput(input=input_data, app_config=executor.activity.app_config),
            task_queue=executor.activity.queue,
            retry_policy=to_temporal_retry_policy(executor.activity.retry_policy),
            schedule_to_close_timeout=to_timedelta(executor.activity.schedule_to_close_timeout),
            start_to_close_timeout=to_timedelta(executor.activity.start_to_close_timeout),
            heartbeat_timeout=to_timedelta(executor.activity.heartbeat_timeout),
            result_type=dict,
        )
        return result
    else:
        raise ValueError("Invalid executor configuration")
