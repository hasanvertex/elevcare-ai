
def create_qr_text(
    elevator_id,
    customer,
    status,
    next_visit,
    technician
):

    return f'''
Elevator: {elevator_id}
Customer: {customer}
Status: {status}
Next Visit: {next_visit}
Technician: {technician}
'''
