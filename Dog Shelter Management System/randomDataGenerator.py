import pandas as pd
import random
from datetime import datetime, timedelta

#DATASET INFO
numberOfShelters = 28
numberOfDogs = 500

#ANIMAL INFO
dogNames = [
    "Milo", "Luna", "Charlie", "Bella", "Max", "Lucy", "Rocky", "Daisy", "Buddy", "Lily",
    "Jack", "Molly", "Toby", "Coco", "Oscar", "Sadie", "Leo", "Maggie", "Simba", "Chloe",
    "Lucky", "Sophie", "Oliver", "Bailey", "Zeus", "Ruby", "Finn", "Nala", "Rex", "Lola",
    "Buster", "Mia", "Duke", "Zoe", "Bruno", "Rosie", "Teddy", "Ellie", "Sam", "Ginger",
    "Benji", "Roxy", "Murphy", "Penny", "Shadow", "Gracie", "Gizmo", "Pepper", "Bear", "Annie",
    "Hunter", "Abby", "Marley", "Hazel", "Diesel", "Olive", "Ace", "Mocha", "Oreo", "Lexi",
    "Ziggy", "Athena", "Jake", "Cleo", "Louie", "Minnie", "Harley", "Belle", "Thor", "Izzy",
    "Winston", "Nina", "Kobe", "Dixie", "Boomer", "Millie", "Archie", "Sasha", "Chester", "Fiona",
    "George", "Cookie", "Tank", "Trixie", "Jasper", "Princess", "Scout", "Kiki", "Benny", "Bonnie",
    "Cash", "Sky", "Moose", "Angel", "Zane", "Kira", "Remy", "Pixie", "Romeo", "Tina",
    "Rusty", "Rita", "Chance", "Poppy", "Hank", "Nikki", "Blue", "Tara", "Zorro", "Sandy",
    "Tyson", "Maya", "King", "Lacey", "Ranger", "Honey", "Apollo", "Muffin", "Axel", "Dora",
    "Baxter", "Pearl", "Arlo", "Fluffy", "Sammy", "Snowy", "Einstein", "Cupcake", "Rambo", "Demi",
    "Indy", "Juno", "Yogi", "Fifi", "Ronnie", "Toffee", "Smokey", "Queenie", "Joey", "Nessie",
    "Riley", "Mochi", "Vito", "Minnie", "Colt", "Candy", "Jett", "Gala", "Lou", "Peach",
    "Turbo", "Dudu", "Melo", "Cinnamon", "Bolt", "Kiwi", "Flash", "Sprinkles", "Coco", "Pika",
    "Jet", "Sushi", "Maxi", "Nemo", "Tango", "Minty", "Whiskey", "Waffle", "Draco", "Cherry",
    "Frodo", "Taffy", "Groot", "Dudu", "Spike", "Churro", "Storm", "Latte", "Vader", "S'mores",
    "Marsh", "Figaro", "Bugsy", "Bambi", "Casper", "Clover", "Nacho", "Maple", "Zuzu", "Bingo",
    "Tiger", "Bubbles", "Ringo", "Misty", "Smudge", "Kovu", "Sparky", "Snowball", "Cloud", "Otis",
    "Mamba", "Pumpkin", "Fang", "Cuddles", "Pickles", "Tofu", "Skittles", "Whiskers", "Kermit", "Beans",
    "Fudge", "Choco", "Snickers", "Wiggles", "Biscuit", "Echo", "Freckles", "Garfield", "Raisin", "Twix",
    "Mittens", "Snuggles", "Hiccup", "Nugget", "Snappy", "Olaf", "Marble", "Yoda", "Tater", "Spud",
    "Corky", "Boom", "Socks", "Basil", "Chippy", "Shaggy", "Cricket", "Jelly", "Zipper", "Blitz"
]
breeds = [
    "Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Poodle",
    "Beagle", "Rottweiler", "Yorkshire Terrier", "Boxer", "Dachshund", "Great Dane",
    "Siberian Husky", "Doberman Pinscher", "Shih Tzu", "Australian Shepherd", "Pomeranian",
    "Cocker Spaniel", "Chihuahua", "French Bulldog", "Border Collie", "Boston Terrier",
    "Cane Corso", "Miniature Schnauzer", "English Springer Spaniel", "Maltese", "Basset Hound",
    "Bernese Mountain Dog", "Australian Cattle Dog", "Newfoundland", "Akita", "Collie",
    "Weimaraner", "Bichon Frise", "Alaskan Malamute", "Airedale Terrier", "Havanese",
    "Vizsla", "Whippet", "St. Bernard", "Shiba Inu", "Scottish Terrier", "Bullmastiff",
    "Cavalier King Charles Spaniel", "Rhodesian Ridgeback", "Old English Sheepdog",
    "Belgian Malinois", "Papillon", "Bloodhound", "Samoyed", "Irish Setter", "Japanese Chin",
    "American Eskimo Dog", "Chinese Crested", "Norwegian Elkhound", "Tibetan Terrier",
    "Chow Chow", "Basenji", "Lhasa Apso", "Pointer", "Pekingese", "Toy Fox Terrier",
    "Saluki", "Afghan Hound", "Keeshond", "English Mastiff", "Leonberger", "Irish Wolfhound",
    "Belgian Tervuren", "Anatolian Shepherd Dog", "Boerboel", "Neapolitan Mastiff",
    "Great Pyrenees", "Tibetan Mastiff", "Spinone Italiano", "Manchester Terrier",
    "Norwich Terrier", "Sealyham Terrier", "Welsh Terrier", "Brussels Griffon",
    "Coton de Tulear", "Glen of Imaal Terrier", "Bedlington Terrier", "Silky Terrier",
    "Redbone Coonhound", "Treeing Walker Coonhound", "Plott Hound", "Bluetick Coonhound",
    "American Foxhound", "Black and Tan Coonhound", "Dogo Argentino", "Belgian Sheepdog",
    "Belgian Laekenois", "Lagotto Romagnolo", "Norfolk Terrier", "Finnish Spitz",
    "Swedish Vallhund", "Schipperke", "Ibizan Hound", "Pharaoh Hound", "Xoloitzcuintli",
    "Otterhound", "Komondor", "Kuvasz", "Sloughi", "American Staffordshire Terrier",
    "Staffordshire Bull Terrier", "Bull Terrier", "Miniature Bull Terrier", "English Foxhound",
    "Clumber Spaniel", "English Toy Spaniel", "Field Spaniel", "Sussex Spaniel", "Tibetan Spaniel",
    "Wirehaired Pointing Griffon", "German Shorthaired Pointer", "German Wirehaired Pointer",
    "Spinone Italiano", "Nova Scotia Duck Tolling Retriever", "Curly-Coated Retriever",
    "Flat-Coated Retriever", "Chesapeake Bay Retriever", "American Water Spaniel",
    "Boykin Spaniel", "English Setter", "Gordon Setter", "Bluetick Coonhound", "Catahoula Leopard Dog",
    "Carolina Dog", "Korean Jindo", "Thai Ridgeback", "Peruvian Inca Orchid", "Russian Toy",
    "Puli", "Polish Lowland Sheepdog", "Spanish Water Dog", "Portuguese Water Dog"
]
genders = ['Erkek', 'Disi']
conditions = ['Saglikli','Hasta', 'Tedavi Ediliyor']

#SHELTER INFO
shelterNames = [
    "Cankaya Karatas Gecici Hayvan Bakimevi",
    "Golbasi Gecici Hayvan Bakimevi ve Rehabilitasyon Merkezi",
    "Sincan Gecici Hayvan Bakimevi ve Rehabilitasyon Merkezi",
    "Patipark Hayvan Barinagi",
    "Etimesgut Hayvan Barinagi",
    "Cankaya Cemil Erkok Rehabilitasyon Merkezi",
    "Esenyurt Hayvan Bakimevi ve Rehabilitasyon Merkezi",
    "Altindag Belediyesi Hayvan Barinagi",
    "Esenyurt Hayvan Bakimevi ve Rehabilitasyon Merkezi",
    "Yedikule Hayvan Barinagi",
    "Tuzla Hayvan Barinagi",
    "Kadikoy Belediyesi Gecici Hayvan Bakim Merkezi",
    "Sile Hayvan Barinagi",
    "Buyukcekmece Sahipsiz Hayvanlar Bakim Merkezi",
    "Gumusdere Sahipsiz Hayvan Bakimevi",
    "Tepeoren Sahipsiz Hayvan Bakimevi",
    "Orhanli Sahipsiz Hayvan Bahceli Yasam Alani",
    "Kemerburgaz Sahipsiz Hayvan Bakimevi",
    "Beykoz Barinagi",
    "Mimarsinan Barinagi",
    "Seferihisar Hayvan Barinagi",
    "Selcuk Hayvan Barinagi",
    "Isikkent Gecici Kopek Bakimevi",
    "Pako Sokak Hayvanlari Sosyal Yasam Kampusu",
    "Buca Sokak Hayvanlari Rehabilitasyon Merkezi",
    "Foca Belediyesi Gecici Bakimevi",
    "Guzelbahce Gecici Kopek Bakimevi",
    "Patipark Hayvan Bakim ve Rehabilitasyon Merkezi"
]
shelterLocations = [
    "Cankaya, Ankara",
    "Gölbasi, Ankara",
    "Sincan, Ankara",
    "Ayas, Ankara",
    "Etimesgut, Ankara",
    "Cankaya, Ankara",
    "Mamak, Ankara",
    "Altindag, Ankara",
    "Esenyurt, Istanbul",
    "Fatih, Istanbul",
    "Tuzla, Istanbul",
    "Atasehir, Istanbul",
    "Sile, Istanbul",
    "Buyukcekmece, Istanbul",
    "Sariyer, Istanbul",
    "Pendik, Istanbul",
    "Tuzla, Istanbul",
    "Eyupsultan, Istanbul",
    "Beykoz, Istanbul",
    "Mimarsinan, Istanbul",
    "Seferihisar, Izmir",
    "Selcuk, Izmir",
    "Bornova, Izmir",
    "Bornova, Izmir",
    "Buca, Izmir",
    "Foca, Izmir",
    "Guzelbahce, Izmir",
    "Aliaga, Izmir"
]
shelterCapacity = [
    6000,
    1500,
    2200,
    1000,
    200,
    470,
    250,
    150,
    700,
    2000,
    300,
    350,
    150,
    2500,
    1300,
    1200,
    500,
    400,
    1600,
    150,
    250,
    600,
    550,
    1500,
    100,
    200,
    150,
    250
]

#EMPLOYEE INFO
employeeFirstNames = [
    "Ahmet", "Mehmet", "Fatma", "Ayşe", "Emre", "Elif", "Can", "Deniz", "Mert", "Zeynep",
    "Hakan", "Hasan", "Hüseyin", "İsmail", "Burak", "Özge", "Cem", "Serkan", "Selin", "Ece",
    "Yusuf", "Sinem", "İrem", "Berke", "Ömer", "Merve", "Esra", "Ali", "Şule", "Gökhan",
    "Murat", "Büşra", "Eren", "İlker", "Furkan", "Nazlı", "Seda", "Volkan", "Gizem", "Okan",
    "Derya", "Selçuk", "Ceyda", "Ebru", "Suat", "Kadir", "Rabia", "Tuğba", "Oğuz", "Damla",
    "Barış", "Emine", "Sibel", "Cihan", "Ferhat", "Şirin", "Halil", "Aslı", "Engin", "Nazan",
    "Volkan", "Özlem", "Tuba", "Yasemin", "Fatih", "Hülya", "Kemal", "Elvan", "Murat", "Figen",
    "Tolga", "Sevgi", "Levent", "Gamze", "İsmail", "Hande", "Çağlar", "Selma", "Onur", "Hatice",
    "Ali", "Nihat", "Serap", "Süleyman", "Nesrin", "Baran", "Leyla", "Kaan", "Nilay", "Deniz",
    "Arda", "Gülay", "Veli", "Pelin", "Suat", "Gül", "Ozan", "Nermin", "Fikret", "Bahar",
    "Ramazan", "Özkan", "Naci", "Şenay", "Efe", "Gülşah", "Berk", "Necla", "Fahri", "Selin",
    "Uğur", "Feride", "İbrahim", "Sevil", "Serhat", "Yeliz", "Mevlüt", "Fatma", "Halime", "Cansu",
    "Melek", "Deniz", "Seda", "Hakan", "Sibel", "Emir", "Bahar", "Alper", "Gülizar", "Koray",
    "Cemre", "Zeki", "Dilek", "Burcu", "Sinan", "Mine", "Barış", "Şebnem", "Ersin", "Şule",
    "Gökçe", "Fırat", "Duygu", "Tolga", "Sevim", "Ferit", "Pelin"
]
employeeLastNames = [
    "Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Yıldız", "Öztürk", "Aydın", "Arslan", "Doğan",
    "Kurt", "Koç", "Özdemir", "Polat", "Güneş", "Acar", "Erdoğan", "Aksoy", "Çetin", "Kaplan",
    "Yalçın", "Bulut", "Özkan", "Aslan", "Taş", "Kılıç", "Bozkurt", "Erdem", "Kara", "Özer",
    "Çakır", "Duran", "Tekin", "Gür", "Yücel", "Yavuz", "Sever", "Özkan", "Kalkan", "Özkan",
    "Arıkan", "Yılmazer", "Demirtaş", "Sönmez", "Altun", "Çınar", "Gül", "Öztürk", "Eren", "Erkan",
    "Karaaslan", "Kalkan", "Sarı", "Uslu", "Özkan", "Aktaş", "Polat", "Çelik", "Kurtuluş", "Uçar",
    "Yıldırım", "Gök", "Aydın", "Kara", "Çakmak", "Özer", "Başaran", "Savaş", "Güler", "Kurt",
    "Erdem", "Kara", "Özdemir", "Yalçın", "Koç", "Gündüz", "Çetin", "Kaplan", "Demirci", "Akdoğan",
    "Özkan", "Arslan", "Şahin", "Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Yıldız", "Öztürk",
    "Aydın", "Arslan", "Doğan", "Kurt", "Koç", "Özdemir", "Polat", "Güneş", "Acar", "Erdoğan",
    "Aksoy", "Çetin", "Kaplan", "Yalçın", "Bulut", "Özkan", "Aslan", "Taş", "Kılıç", "Bozkurt",
    "Erdem", "Kara", "Özer", "Çakır", "Duran", "Tekin", "Gür", "Yücel", "Yavuz", "Sever",
    "Özkan", "Kalkan", "Özkan", "Arıkan", "Yılmazer", "Demirtaş", "Sönmez", "Altun", "Çınar",
    "Gül", "Öztürk", "Eren", "Erkan", "Karaaslan", "Kalkan", "Sarı", "Uslu", "Özkan", "Aktaş",
    "Polat", "Çelik", "Kurtuluş", "Uçar", "Yıldırım", "Gök", "Aydın", "Kara", "Çakmak"
]
employeeTasks = ["Veteriner", "Bakici", "Temizlik Gorevlisi", "Yonetici", "Gonullu", "Teknik Personel"]

#VET INFO
vetSpecialties = [
    "Dahiliye",            
    "Cerrahi",              
    "Doğum ve Jinekoloji",  
    "Parazitoloji",        
    "Mikrobiyoloji",       
    "Hayvan Besleme",       
    "Epidemiyoloji",       
    "Patoloji",             
    "Farmakoloji",         
    "Radyoloji",            
    "Rehabilitasyon",      
    "Anesteziyoloji",       
    "Zootekni",            
    "Yoğun Bakım",          
    "Acil Müdahale",        
]

#INSPECTION INFO
diagnoses = [
    "Parvovirüs enfeksiyonu",
    "Distemper",
    "Kennel öksürüğü",
    "Lyme hastalığı",
    "Dermatit",
    "Kulak enfeksiyonu",
    "Parazit enfeksiyonu",
    "Gastrit",
    "Diyabet",
    "Kalp hastalığı",
    "Böbrek yetmezliği",
    "Hipotiroidi",
    "Diz kapağı çıkığı",
    "Kanser"
]
treatments = [
    "Sıvı tedavisi, antiviral ilaçlar, destekleyici bakım",
    "Antiviral ve antibiyotik tedavisi, aşı",
    "Antibiyotikler, öksürük kesici ilaçlar, dinlenme",
    "Antibiyotikler, kene önleyici ilaçlar",
    "Topikal kortikosteroidler, antihistaminikler",
    "Antibiyotik damlalar, kulak temizliği",
    "Parazit önleyici ilaçlar, düzenli bakım",
    "Antasitler, diyet değişikliği, proton pompa inhibitörleri",
    "İnsülin tedavisi, diyet ve egzersiz",
    "İlaç tedavisi, diyet, egzersiz ve düzenli kontroller",
    "Diyet değişikliği, diyaliz, destekleyici bakım",
    "Tiroid hormonu replasman tedavisi",
    "Cerrahi müdahale, fizik tedavi, ağrı kesiciler",
    "Kemoterapi, radyoterapi, cerrahi müdahale"
]

def randomDate(start_year=2020, end_year=2024):
    startDate = datetime(start_year, 1, 1)
    endDate = datetime(end_year, 12, 31)
    delta = endDate - startDate
    randomDays = random.randint(0, delta.days)
    return (startDate + timedelta(days=randomDays)).date()

def randomPartition(total, parts):
    cuts = sorted(random.sample(range(1, total), parts - 1))
    partsList = []
    prev = 0
    for cut in cuts:
        partsList.append(cut - prev)
        prev = cut
    partsList.append(total - prev)
    return partsList

def generateAnimalData(numberOfDogs, numberOfShelters):
    shelterCounts = randomPartition(numberOfDogs, numberOfShelters)

    shelterIds = []
    for shelterId, count in enumerate(shelterCounts, start=1):
        shelterIds.extend([shelterId] * count)

    datas = []
    for i in range(1, numberOfDogs + 1):
      data = {
          'HayvanId': i,
          'Ad': random.choice(dogNames),
          'Tur': random.choice(breeds),
          'Cinsiyet': random.choice(genders),
          'Yas': random.randint(0, 15),
          'SaglikDurumu': random.choice(conditions),
          'GelisTarihi': randomDate(),
          'BarinakId': shelterIds[i-1]
      }
      datas.append(data)
    return datas

def generateShelterData(numberOfShelters):
    datas = []
    for i in range(1, numberOfShelters + 1):
      data = {
          'BarinakId': i,
          'Ad': shelterNames[i-1],
          'Konum': shelterLocations[i-1],
          'Kapasite': shelterCapacity[i-1],
          'Sifre':i
      }
      datas.append(data)
    return datas

def generateEmployeeData(numberOfShelters):
    datas = []
    personelId = 1
    for barinakId in range(1, numberOfShelters + 1):
        for i in range(5): 
            data = {
                'PersonelId': personelId,
                'Ad': random.choice(employeeFirstNames),
                'Soyad': random.choice(employeeLastNames),
                'Gorev': employeeTasks[i],  
                'CalismaTarihi': randomDate(),
                'BarinakId': barinakId
            }
            datas.append(data)
            personelId += 1
    return datas

def generateVetData(employeeData):
    datas = []
    for emp in employeeData:
        if emp['Gorev'] == 'Veteriner':
            data = {
                'VetId': emp['PersonelId'],
                'Ad': emp['Ad'],
                'Soyad': emp['Soyad'],
                'Uzmanlik':random.choice(vetSpecialties)
            }
            datas.append(data)
    return datas

def generateInspectionData(animalData, personelData):
    muayeneId = 1
    datas = []

    shelterToVet = {
        personel['BarinakId']: personel['PersonelId']
        for personel in personelData
        if personel['Gorev'] == 'Veteriner'
    }

    treatmentDict = dict(zip(diagnoses, treatments))

    treatedAnimals = [animal for animal in animalData if animal['SaglikDurumu'] == 'Tedavi Ediliyor']

    for animal in treatedAnimals:
        barinakId = animal['BarinakId']

        veterinerId = shelterToVet.get(barinakId)

        if veterinerId is None:
            continue

        diagnose = random.choice(diagnoses)
        treatment = treatmentDict.get(diagnose, "Bilinmeyen Tedavi")

        data = {
            'MuayeneId': muayeneId,
            'HayvanId': animal['HayvanId'],
            'VeterinerId': veterinerId,
            'Tarih': randomDate(),
            'Teshis': diagnose,
            'Tedavi': treatment
        }

        datas.append(data)
        muayeneId += 1

    return datas


dfEmployees = pd.DataFrame(generateEmployeeData(numberOfShelters))
dfAnimals = pd.DataFrame(generateAnimalData(numberOfDogs, numberOfShelters))
dfShelters = pd.DataFrame(generateShelterData(numberOfShelters))
dfVets = pd.DataFrame(generateVetData(dfEmployees.to_dict('records')))
dfInspections = pd.DataFrame(generateInspectionData(dfAnimals.to_dict('records'),dfEmployees.to_dict('records')))

with pd.ExcelWriter('Data/data.xlsx', engine='openpyxl') as writer:
    dfAnimals.to_excel(writer, sheet_name='hayvan', index=False)
    dfShelters.to_excel(writer, sheet_name='barinak', index=False)
    dfEmployees.to_excel(writer, sheet_name = 'personel', index = False)
    dfVets.to_excel(writer, sheet_name = 'veteriner', index = False)
    dfInspections.to_excel(writer, sheet_name = 'muayene', index = False)

