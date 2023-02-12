roll = [3173,3120,3123]
for i in roll:
    cursor.execute("select * from st_details where rollno= '%s'" %roll[i])
print()