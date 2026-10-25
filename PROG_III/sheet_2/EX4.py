dict = {
    "class": {
        "student": {
        "name": "Mike",
            "marks": {
            "physics": 70,
            "history": 80
            }
        }
    }
}

print(f"Value from key 'history' is: {dict.get('class').get('student').get('marks').get('history')}")

dict.update({"class": {"student": {"name":"Mark"}}})

print(f"Updated Name: {dict.get('class').get('student').get('name')}")