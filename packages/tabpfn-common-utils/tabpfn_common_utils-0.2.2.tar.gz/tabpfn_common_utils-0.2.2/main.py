from tabpfn_common_utils.telemetry.core.service import ProductTelemetry
from tabpfn_common_utils.telemetry.core.events import PingEvent, FitEvent, PredictEvent
import os
from tabpfn_common_utils.telemetry.core.state import _state_path, get_property

def clear_state_file():
    """Delete the telemetry state file from disk."""
    state_file = _state_path()
    
    try:
        if os.path.exists(state_file):
            os.remove(state_file)
            print(f"Deleted state file: {state_file}")
        else:
            print(f"State file does not exist: {state_file}")
    except Exception as e:
        print(f"Error deleting state file: {e}")




if __name__ == "__main__":


    from tabpfn_common_utils.telemetry.interactive.flows import opt_in

    opt_in()

    # Clear the state file

    telemetry = ProductTelemetry()
    
    # Generate 100 examples of Fit and Predict events
    events = []

    # Create diverse examples with different tasks, sizes, and durations
    import random

    results = {}

    from datetime import datetime, timezone, timedelta
    from tabpfn_common_utils.telemetry.core.state import set_property
    
    for _ in range(1000):

        clear_state_file()
        
        utc_now = datetime.now(timezone.utc)
        install_date = utc_now - timedelta(days=30)
        set_property("install_date", install_date)

        temp_results = []
        for i in range(100):
            # Alternate between classification and regression tasks
            task = "classification" if i % 2 == 0 else "regression"
            
            # Generate realistic dataset sizes
            num_rows = random.randint(100, 50000)
            num_columns = random.randint(5, 200)
            
            # Generate realistic duration in milliseconds (10ms to 30 seconds)
            duration_ms = random.randint(10, 10000)
            
            # Alternate between Fit and Predict events
            if i % 2 == 0:
                event = FitEvent(
                    task=task,
                    num_rows=num_rows,
                    num_columns=num_columns,
                    duration_ms=duration_ms
                )
            else:
                event = PredictEvent(
                    task=task,
                    num_rows=num_rows,
                    num_columns=num_columns,
                    duration_ms=duration_ms
                )
            
            # Determine if the event should be passed through
            temp_results.append(telemetry._pass_through(event))

        install_id = get_property("install_id", data_type=str)
        results[install_id] = temp_results


        
    pass
    
    # Print first 10 events to verify
    print(f"Generated {len(events)} telemetry events")
    for i, event in enumerate(events[:10]):
        print(f"Event {i+1}: {event.name} - {event}")

    # Send each event individually
    for event in events:
        telemetry.capture(event)
    
    # Flush the telemetry queue
    telemetry.flush()