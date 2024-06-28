absender = input("Wer ist der Absender? ")


def generate_newsletter(absender):
    name = input("An wen geht die Nachricht? ")
    print(f"Hallo {name}")
    print("")
    print("Mit dieser E-Mail möchte ich dich über meine neue Adresse informieren.")
    print("")
    print("Musterstraße 123")
    print("12345 Musterhausen")
    print("Viele Grüße")
    print("")
    print(f"{absender}")

generate_newsletter(absender)
generate_newsletter(absender)
generate_newsletter(absender)
generate_newsletter(absender)