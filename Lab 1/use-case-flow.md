# Use-Case Flow Specification

## Use Case: Generate Optimized Collection Route

### Primary Actor

Sanitation Supervisor

### Preconditions

1. Smart bins are registered in the system.
2. The system has received current fill-level data from the smart bins.
3. Garbage trucks are available for collection.

### Postconditions

1. An optimized collection route is generated.
2. Eligible bins are included in the collection route.
3. The generated route can be assigned to a Truck Driver.

### Main Success Scenario

1. The Sanitation Supervisor logs into the sanitation management portal.
2. The Supervisor requests generation of the daily collection route.
3. The system retrieves the latest fill-level data from the smart bins.
4. The system identifies bins whose fill level exceeds 80%.
5. The system identifies available garbage trucks.
6. The system calculates an optimized collection route.
7. The system displays the generated route to the Sanitation Supervisor.
8. The Supervisor assigns the route to a Truck Driver.
9. The Truck Driver views the assigned collection route.

### Alternate Flow

If no smart bins have exceeded the 80% fill threshold, the system does not generate a collection route and informs the Sanitation Supervisor that no collection is currently required.

### Include Relationship

Generate Optimized Collection Route
includes
Identify Bins Above 80% Fill Level

### Extend Relationship

Track Citizen Complaint
is extended by
Handle Missed Pickup Complaint
