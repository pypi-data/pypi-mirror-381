import pyarrow as pa

# Define inner struct for TPSR/SPT time-alt-az entries, with timestamp type
tps_item = pa.struct(
    [
        pa.field(
            "time", pa.timestamp("us", tz="UTC")
        ),  # timestamp with microsecond precision
        pa.field("alt", pa.float64()),
        pa.field("az", pa.float64()),
    ]
)

# Define inner struct for observation_periods entries
obs_item = pa.struct(
    [
        pa.field("value", pa.list_(pa.float64())),
        pa.field("unit", pa.string()),
    ]
)

# Top-level schema for TPSR/SPT events
event_schema = pa.schema(
    [
        pa.field("publisher", pa.string()),
        pa.field("publisher_id", pa.string()),
        pa.field("event_type", pa.string()),
        pa.field("event_id", pa.string()),
        pa.field("priority", pa.int64()),
        pa.field("params", pa.map_(pa.string(), pa.string())),
        pa.field("ra", pa.float64()),
        pa.field("dec", pa.float64()),
        pa.field("detection_time", pa.timestamp("us", tz="UTC")),
        pa.field("tpsrspt", pa.list_(tps_item)),
        pa.field("observation_periods", pa.list_(obs_item)),
    ]
)
