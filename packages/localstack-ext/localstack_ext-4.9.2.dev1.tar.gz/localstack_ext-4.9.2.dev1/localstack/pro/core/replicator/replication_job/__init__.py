from localstack.pro.core.replicator.replication_job.batch_replication_job import (
    BatchResourceReplicationJob,
)
from localstack.pro.core.replicator.replication_job.mock_replication_job import MockReplicationJob
from localstack.pro.core.replicator.replication_job.single_replication_job import (
    SingleResourceReplicationJob,
)

REPLICATIONS_JOBS = {
    replication_job.type: replication_job
    for replication_job in (
        MockReplicationJob,
        SingleResourceReplicationJob,
        BatchResourceReplicationJob,
    )
}

__all__ = ["REPLICATIONS_JOBS"]
