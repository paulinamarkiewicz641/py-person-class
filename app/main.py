class Person:
    people = {}
    def __int__(self, name: string, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self
    pass

@staticmethod
def create_person_list(people: list) -> list:
    persons = [Person(person_dict["name"], person_dict["age"]) for person_dict in people]
        

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)
        if spouse_name:
            setattr(person, spouse_key, Person.people[spouse_name])
        
    return persons
