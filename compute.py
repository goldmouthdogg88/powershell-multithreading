# You are tasked with creating 1000 new accounts,
# using the createUserAccount command.
# It takes 3 seconds to create a new user.

accounts_to_create = 1000
time_to_create_account = 3 # seconds
run_time = accounts_to_create * time_to_create_account



print(str(run_time / 60) + ' minutes')
