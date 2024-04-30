from Spotfire.Dxp.Application.Scripting import ScriptDefinition
from System import TimeSpan, DateTime

def UpdatePeriodOrEndDate(doc):
    start_date = doc.Properties["StartDate"]
    period = doc.Properties["Period"]
    end_date = doc.Properties["EndDate"]
    
    if start_date is None:
        raise ValueError("Start date must be set.")

    if period is not None and end_date is None:
        # Directly set end date from period if end date is not provided
        doc.Properties["EndDate"] = start_date.AddDays(period)
    elif end_date is not None and period is None:
        # Directly set period from end date if period is not provided
        if end_date < start_date:
            raise ValueError("End date cannot be before start date.")
        delta = end_date - start_date
        doc.Properties["Period"] = delta.Days
    elif period is not None and end_date is not None:
        # Adjust the end date if there is a discrepancy
        calculated_end_date = start_date.AddDays(period)
        if calculated_end_date != end_date:
            doc.Properties["EndDate"] = start_date.AddDays(period)
    else:
        # Both period and end date are None, set a default or raise an error
        raise ValueError("Either period or end date must be provided.")

# Example of how to invoke the function, assuming 'Document' is your Spotfire Document context
UpdatePeriodOrEndDate(Document)