from enum import StrEnum


class AgentTelemetryFields(StrEnum):
    """AI Agent telemetry fields."""

    # Agent identity
    AGENT_ID = "agent.id"
    AGENT_NAME = "agent.name"
    AGENT_VERSION = "agent.version"
    AGENT_TYPE = "agent.type"  # autonomous, reactive, cognitive, multi_agent
    AGENT_ROLE = "agent.role"  # coordinator, executor, specialist, orchestrator

    # Agent lifecycle
    AGENT_STATE = "agent.state"  # initializing, idle, processing, error, shutdown
    AGENT_UPTIME_SECONDS = "agent.uptime_seconds"
    AGENT_TASKS_COMPLETED = "agent.tasks_completed"
    AGENT_TASKS_FAILED = "agent.tasks_failed"
    AGENT_LAST_ACTIVITY_TIME = "agent.last_activity_time"

    # Task execution
    TASK_ID = "agent.task.id"
    TASK_TYPE = "agent.task.type"
    TASK_PRIORITY = "agent.task.priority"  # low, normal, high, critical
    TASK_STATUS = "agent.task.status"  # pending, running, completed, failed, cancelled
    TASK_DURATION_MS = "agent.task.duration_ms"
    TASK_START_TIME = "agent.task.start_time"
    TASK_END_TIME = "agent.task.end_time"
    TASK_RETRY_COUNT = "agent.task.retry_count"

    # Decision making
    DECISION_ID = "agent.decision.id"
    DECISION_TYPE = "agent.decision.type"
    DECISION_CONFIDENCE = "agent.decision.confidence"  # 0.0-1.0
    DECISION_REASONING = "agent.decision.reasoning"
    DECISION_ALTERNATIVES_COUNT = "agent.decision.alternatives_count"
    DECISION_TIME_MS = "agent.decision.time_ms"

    # Learning & adaptation
    LEARNING_SESSION_ID = "agent.learning.session_id"
    LEARNING_TYPE = "agent.learning.type"  # supervised, reinforcement, unsupervised
    LEARNING_ACCURACY = "agent.learning.accuracy"
    LEARNING_LOSS = "agent.learning.loss"
    LEARNING_EPOCHS = "agent.learning.epochs"
    LEARNING_DATASET_SIZE = "agent.learning.dataset_size"

    # Memory & knowledge
    MEMORY_USAGE_BYTES = "agent.memory.usage_bytes"
    MEMORY_WORKING_SIZE = "agent.memory.working_size"
    MEMORY_LONG_TERM_SIZE = "agent.memory.long_term_size"
    KNOWLEDGE_BASE_SIZE = "agent.knowledge_base.size"
    KNOWLEDGE_BASE_VERSION = "agent.knowledge_base.version"

    # Communication & coordination
    MESSAGE_ID = "agent.message.id"
    MESSAGE_TYPE = "agent.message.type"  # request, response, broadcast, notification
    MESSAGE_SENDER = "agent.message.sender"
    MESSAGE_RECEIVER = "agent.message.receiver"
    MESSAGE_SIZE_BYTES = "agent.message.size_bytes"
    MESSAGE_LATENCY_MS = "agent.message.latency_ms"

    # Multi-agent coordination
    SWARM_ID = "agent.swarm.id"
    SWARM_SIZE = "agent.swarm.size"
    SWARM_ROLE = "agent.swarm.role"  # leader, follower, peer
    CONSENSUS_ROUND = "agent.consensus.round"
    CONSENSUS_AGREEMENT = "agent.consensus.agreement"  # true, false

    # Performance metrics
    THROUGHPUT_TASKS_PER_SECOND = "agent.throughput.tasks_per_second"
    RESPONSE_TIME_MS = "agent.response_time_ms"
    SUCCESS_RATE = "agent.success_rate"  # 0.0-1.0
    ERROR_RATE = "agent.error_rate"  # 0.0-1.0

    # Resource utilization
    CPU_USAGE_PERCENT = "agent.cpu.usage_percent"
    MEMORY_USAGE_PERCENT = "agent.memory.usage_percent"
    GPU_USAGE_PERCENT = "agent.gpu.usage_percent"
    GPU_MEMORY_USAGE_BYTES = "agent.gpu.memory.usage_bytes"

    # Goal & planning
    GOAL_ID = "agent.goal.id"
    GOAL_TYPE = "agent.goal.type"
    GOAL_PRIORITY = "agent.goal.priority"
    GOAL_STATUS = "agent.goal.status"  # active, achieved, abandoned, blocked
    PLAN_ID = "agent.plan.id"
    PLAN_STEPS_COUNT = "agent.plan.steps_count"
    PLAN_PROGRESS = "agent.plan.progress"  # 0.0-1.0
