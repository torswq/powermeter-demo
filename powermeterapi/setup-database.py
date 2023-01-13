import random, uuid
lista_nombres = ["Juan", "Alberto", "Rodolfo", "Mondolfo", "Platon", "Greta", "Jose", "Franco", "Noelia", "Esteban"]
for i in range(0, 50):
    person_measurer = Measurer(uuid=str(uuid.uuid4()),name=f"{lista_nombres[random.randrange(0,len(lista_nombres))]}{random.randrange(0,999999)}", consumption=0)
    person_measurer.save()
    for i in range(1,11):
        consumption = random.randrange(100,1000)
        person_measurer.consumption=consumption
        person_measurer.save(update_fields=["consumption"])