#programa de consumo de una API (PokeAPI)
import requests

import tkinter as tk


def Poke_info(pokemon): # ------------> funcion para consumir la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" #direccion de la API
    data = requests.get(url)
    
    output_text.delete("1.0", tk.END)

    if data.status_code == 200:#verificacion de estado
     pokemon_data = data.json()#formateo a json
    
     name = pokemon_data["name"]#tomar el nombre del pokemon
     output_text.insert(tk.END, f"Name: {name}\n\n")
     
     output_text.insert(tk.END, "Stats:\n")
     for stat in pokemon_data['stats']:#iterar sobre sus estadisticas y mostrarlas junto a sus valores
         name_stat = stat['stat']['name']
         value_stat = stat['base_stat']
         output_text.insert(tk.END, f"- {name_stat.capitalize()}: {value_stat}\n")
         
         
         
     output_text.insert(tk.END, "abilities:\n")#iterar sobre sus habilidades y mostrarlas
     for abs in pokemon_data['abilities']:
         name_ab = abs['ability']['name']
         output_text.insert(tk.END, f"- {name_ab}\n")
         

     
     
    else:
        output_text.insert(tk.END, f"Error: Pokémon '{pokemon}' not found.")
        

def get_pokemon_data(pokemon_name):
    """Consulta la PokeAPI y devuelve datos estructurados"""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
            "abilities": [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
        }
    else:
        return None  # Pokémon no encontrado
   
   

          