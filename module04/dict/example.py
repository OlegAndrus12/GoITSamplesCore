grade1 = {"Oleg": 2, "Alexx": 3}
grade2 = {"Nastya": 5, "Sergey": 4}
grade3 = {"Alex": 4, "Andry": 5}

result = {}

for d in (grade1, grade2, grade3):
    result.update(d)

print(result)


"""
Метод: format
-------------
Первая цифра в номере пластиковой карты означает, к какой платежной системе она относится. Все карты Visa имеют
номер, начинающийся на «4», Mastercard — на «5», а American Express — «3». Если карту выдала не кредитная
организация, номер может начинаться и с других цифр. «1» и «2» — это различные авиалинии, «3» — организации сферы
путешествий и развлечений, «6» — мерчендайзинговые компании, «7» — топливные, «8» — предприятия в сфере
телекоммуникаций, а «9» — это государственные ассигнации. 
"""

pay_system = {
    5: "MasterCard",
    4: "Visa",
    3: "American Express"
}

card_number = ["5375414112345678", "4168757587879876", "216875758787987d"]


def isvalid_card(card):
    return card.isdigit() and len(card) == 16


for card in card_number:
    string = "Номер карты: {:<8} Платежная система: {:^16} карточка валидна: {:>16}"
    print(string.format(card, pay_system.get(
        int(card[0]), 'Unknown'), str(isvalid_card(card))))