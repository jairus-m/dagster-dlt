from dagster import Definitions, load_assets_from_modules

from .assets import activities, dbt
from .resources import database_resource, dbt_resource
from .jobs import activities_update_job
from .schedules import activities_update_schedule

activities_assets = load_assets_from_modules([activities])
analytics_dbt_assets = load_assets_from_modules(modules=[dbt]) 

all_jobs = [activities_update_job]
all_schedules = [activities_update_schedule]

defs = Definitions(
    assets=activities_assets+ analytics_dbt_assets,
    resources={
        "database": database_resource,
        "dbt": dbt_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules,
)