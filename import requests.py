import requests

API_KEY = "a1f270fb-cb7d-48c2-87a8-90b5e4d1506e"  

def calcular_viaje(origen, destino):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen, destino],
        "vehicle": "car",
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    r = requests.get(url, params=params)

    if r.status_code != 200:
        print("❌ Error al consultar la API.")
        print("Código:", r.status_code)
        print("Respuesta:", r.text)
        return

    data = r.json()
    ruta = data["paths"][0]

    distancia = round(ruta["distance"] / 1000, 2)
    duracion = int(ruta["time"] / 1000)
    horas = duracion // 3600
    minutos = (duracion % 3600) // 60
    segundos = duracion % 60
    combustible = round(distancia / 12, 2)

    print(f"\n📍 Distancia: {distancia:.2f} km")
    print(f"⏱ Duración: {horas}h {minutos}m {segundos}s")
    print(f"⛽ Combustible estimado: {combustible:.2f} litros")

    print("\n🗺 Instrucciones:")
    for paso in ruta["instructions"]:
        print(f"- {paso['text']}")

while True:
    origen = input("\nCiudad de origen (o 'q' para salir): ")
    if origen.lower() == "q":
        break

    destino = input("Ciudad de destino: ")
    if destino.lower() == "q":
        break

    calcular_viaje(origen, destino)

print("\n👋 Fin del programa.")
