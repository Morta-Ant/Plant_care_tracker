#2-3 times week = 2 days
#7 days = 7 days
#7-14 days = 10 days
#14-21 days = 17 days

plant_data = [
  {
    "plant_id": 1,
    "common_name": "Snake Plant",
    "scientific_name": "Sansevieria trifasciata",
    "other_name": "Mother-in-law's Tongue",
    "light_level": "low light",
    "watering_frequency": 17,
    "growth_rate": "Medium",
    "maintenance_level": "Low",
    "plant_description": "The Snake Plant is a popular and hardy houseplant known for its sword-shaped leaves.",
    "image": "https://images.unsplash.com/photo-1593482,892,2,90-f5492,7ae1bb6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8c2,5ha2,UlMjBwbGFudHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 2,
    "common_name": "ZZ Plant",
    "scientific_name": "Zamioculcas zamiifolia",
    "other_name": "Zanzibar Gem",
    "light_level": "low light",
    "watering_frequency": 17,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "The ZZ Plant, also known as Zanzibar Gem, is a resilient houseplant with glossy, dark green leaves.",
    "image": "https://images.unsplash.com/photo-162,2,673037877-18ee56d1f990?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8Mnx8WlolMjBQbGFudHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 3,
    "common_name": "Spider Plant",
    "scientific_name": "Chlorophytum comosum",
    "other_name": "Airplane Plant",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "The Spider Plant, also known as Airplane Plant, is an adaptable and easy-to-care-for plant that produces arching, spider-like leaves.",
    "image": "https://images.unsplash.com/photo-16081617792,98-f42,2,56d2,c58d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8NHx8U3BpZGVyJTIwUGxhbnR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 4,
    "common_name": "Peace Lily",
    "scientific_name": "Spathiphyllum spp.",
    "other_name": "Spathe Flower",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Medium",
    "maintenance_level": "Moderate",
    "plant_description": "The Peace Lily, also known as Spathe Flower, is a graceful houseplant with dark green foliage and elegant white flowers.",
    "image": "https://images.pexels.com/photos/14656095/pexels-photo-14656095.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 5,
    "common_name": "Pothos",
    "scientific_name": "Epipremnum aureum",
    "other_name": "Devil's Ivy",
    "light_level": "low light",
    "watering_frequency": 10,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "The Pothos, also known as Devil's Ivy, is a popular trailing houseplant with heart-shaped leaves that come in various colors.",
    "image": "https://images.unsplash.com/photo-159672,4878582,-76f1a8fdc2,4f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MXx8UG90aG9zfGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 6,
    "common_name": "Rubber Plant",
    "scientific_name": "Ficus elastica",
    "other_name": "Rubber Tree",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Medium",
    "maintenance_level": "Moderate",
    "plant_description": "The Rubber Plant, also known as Rubber Tree, is a popular indoor tree with glossy, rubbery leaves.",
    "image": "https://images.unsplash.com/photo-1591656884447-8562,e2,373a66?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8RmljdXMlMjBlbGFzdGljYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 7,
    "common_name": "Monstera",
    "scientific_name": "Monstera deliciosa",
    "other_name": "Swiss Cheese Plant",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "The Monstera, also known as Swiss Cheese Plant, is a popular tropical plant with large, fenestrated leaves.",
    "image": "https://images.pexels.com/photos/58582,35/pexels-photo-58582,35.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 8,
    "common_name": "Fiddle Leaf Fig",
    "scientific_name": "Ficus lyrata",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 7,
    "growth_rate": "Slow",
    "maintenance_level": "Moderate",
    "plant_description": "The Fiddle Leaf Fig is a trendy and striking houseplant with large, violin-shaped leaves.",
    "image": "https://images.pexels.com/photos/885732,4/pexels-photo-885732,4.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 9,
    "common_name": "Aloe Vera",
    "scientific_name": "Aloe barbadensis miller",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 17,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "Aloe Vera is a well-known succulent with fleshy, spiky leaves that contain a soothing gel.",
    "image": "https://images.unsplash.com/photo-1596547609652,-9cf5d8d7692,1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8YWxvZSUyMHZlcmElMjBwbGFudHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 10,
    "common_name": "Chinese Evergreen",
    "scientific_name": "Aglaonema spp.",
    "other_name": "Aglaonema",
    "light_level": "low light",
    "watering_frequency": 10,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "The Chinese Evergreen, also known as Aglaonema, is a popular houseplant with attractive, variegated leaves.",
    "image": "https://images.unsplash.com/photo-162,3910994874-ec52,179c9862,?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8NHx8YWdsYW9uZW1hfGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 11,
    "common_name": "Boston Fern",
    "scientific_name": "Nephrolepis exaltata",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "Moderate",
    "plant_description": "The Boston Fern is a classic and popular choice for hanging baskets.",
    "image": "https://images.pexels.com/photos/5984746/pexels-photo-5984746.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 12,
    "common_name": "Lucky Bamboo",
    "scientific_name": "Dracaena sanderiana",
    "other_name": "Curly Bamboo",
    "light_level": "low light",
    "watering_frequency": 7,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "Lucky Bamboo, also known as Curly Bamboo, is not a bamboo plant but a member of the Dracaena family.",
    "image": "https://images.unsplash.com/photo-1611137884113-d952,b439f985?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8THVja3klMjBCYW1ib2,98ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 13,
    "common_name": "Golden Pothos",
    "scientific_name": "Epipremnum aureum 'Golden'",
    "other_name": "",
    "light_level": "low light",
    "watering_frequency": 10,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "The Golden Pothos is a variety of Pothos with golden-yellow variegation on its leaves.",
    "image": "https://images.unsplash.com/photo-160596670612,8-92,7ad2,c9e2,c8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MXx8RXBpcHJlbW51bSUyMGF1cmV1bXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 14,
    "common_name": "Spider Plant (Variegated)",
    "scientific_name": "Chlorophytum comosum 'Variegatum'",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 7,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "The Variegated Spider Plant is a popular cultivar with green and white-striped leaves.",
    "image": "https://images.pexels.com/photos/5331915/pexels-photo-5331915.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 15,
    "common_name": "African Violet",
    "scientific_name": "Saintpaulia spp.",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 7,
    "growth_rate": "Medium",
    "maintenance_level": "Moderate",
    "plant_description": "The African Violet is a charming flowering houseplant with fuzzy leaves and colorful blooms.",
    "image": "https://images.unsplash.com/photo-1595609169861-8eedf5d2,6662,?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MXx8QWZyaWNhbiUyMFZpb2,xldHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 16,
    "common_name": "Philodendron",
    "scientific_name": "Philodendron spp.",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 7,
    "growth_rate": "Fast",
    "maintenance_level": "Low",
    "plant_description": "Philodendrons are popular vining plants with heart-shaped leaves.",
    "image": "https://images.unsplash.com/photo-1600411833196-7c1f6b1a8b90?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8Mnx8UGhpbG9kZW5kcm9ufGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 17,
    "common_name": "Jade Plant",
    "scientific_name": "Crassula ovata",
    "other_name": "Money Plant",
    "light_level": "bright indirect light",
    "watering_frequency": 17,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "The Jade Plant, also known as Money Plant, is a popular succulent with fleshy, oval-shaped leaves.",
    "image": "https://images.unsplash.com/photo-1616189597001-9046fce2,594d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8Mnx8SmFkZSUyMFBsYW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 18,
    "common_name": "Dieffenbachia",
    "scientific_name": "Dieffenbachia spp.",
    "other_name": "Dumb Cane",
    "light_level": "bright indirect light",
    "watering_frequency": 7,
    "growth_rate": "Medium",
    "maintenance_level": "Low",
    "plant_description": "Dieffenbachia is a tropical plant with attractive variegated leaves.",
    "image": "https://images.unsplash.com/photo-1631556941887-f81ab0ecfda9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8OHx8RGllZmZlbmJhY2,hpYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 19,
    "common_name": "Bird's Nest Fern",
    "scientific_name": "Asplenium nidus",
    "other_name": "",
    "light_level": "bright indirect light",
    "watering_frequency": 2,
    "growth_rate": "Medium",
    "maintenance_level": "Moderate",
    "plant_description": "The Bird's Nest Fern is a tropical fern with wavy, arching fronds.",
    "image": "https://images.unsplash.com/photo-16152,13612,138-4d1195b1c0e7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8NHx8QXNwbGVuaXVtJTIwbmlkdXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 20,
    "common_name": "Parlor Palm",
    "scientific_name": "Chamaedorea elegans",
    "other_name": "",
    "light_level": "low light",
    "watering_frequency": 7,
    "growth_rate": "Slow",
    "maintenance_level": "Low",
    "plant_description": "The Parlor Palm is a small palm plant that can thrive in low light conditions.",
    "image": "https://images.unsplash.com/photo-16872,69111857-3b398711c2,f4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8UGFybG9yJTIwUGFsbXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 21,
    "common_name": "Tomato",
    "scientific_name": "Solanum lycopersicum",
    "other_name": "",
    "light_level": "full sun",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "High",
    "plant_description": "Tomato plants are popular vegetables grown for their delicious and juicy fruits.",
    "image": "https://images.unsplash.com/photo-15674815992,10-9b707e697c42,?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MXx8U2,9sYW51bSUyMGx5Y2,9wZXJzaWN1bXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 22,
    "common_name": "Basil",
    "scientific_name": "Ocimum basilicum",
    "other_name": "",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Fast",
    "maintenance_level": "Moderate",
    "plant_description": "Basil is a popular herb with fragrant leaves, commonly used in cooking.",
    "image": "https://images.unsplash.com/photo-1619805640532,-2,1cce5fe542,b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8Mnx8YmFzaWwlMjBwbGFudHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 23,
    "common_name": "Mint",
    "scientific_name": "Mentha spp.",
    "other_name": "",
    "light_level": "partial shade",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "Moderate",
    "plant_description": "Mint is a refreshing herb with a strong aroma, often used in teas and culinary dishes.",
    "image": "https://images.unsplash.com/photo-1588908933351-eeb8cd4c452,1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8bWludCUyMHBsYW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 24,
    "common_name": "Cucumber",
    "scientific_name": "Cucumis sativus",
    "other_name": "",
    "light_level": "full sun",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "High",
    "plant_description": "Cucumbers are popular vegetables known for their crisp and refreshing taste.",
    "image": "https://images.unsplash.com/photo-151856840362,8-df55701ade9e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MjN8fGN1Y3VtYmVyJTIwcGxhbnR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 25,
    "common_name": "Lettuce",
    "scientific_name": "Lactuca sativa",
    "other_name": "",
    "light_level": "partial shade",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "High",
    "plant_description": "Lettuce is a leafy green vegetable commonly used in salads and sandwiches.",
    "image": "https://images.unsplash.com/photo-15989982,55396-9c02,89d33304?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8M3x8bGV0dHVjZSUyMHBsYW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 26,
    "common_name": "Carrot",
    "scientific_name": "Daucus carota subsp. sativus",
    "other_name": "",
    "light_level": "partial shade",
    "watering_frequency": 7,
    "growth_rate": "Slow",
    "maintenance_level": "Moderate",
    "plant_description": "Carrots are root vegetables known for their sweet and crunchy texture.",
    "image": "https://images.unsplash.com/photo-163942,7444459-85a1b6ac2,d68?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8MTF8fGNhcnJvdHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 27,
    "common_name": "Bell Pepper",
    "scientific_name": "Capsicum annuum",
    "other_name": "",
    "light_level": "full sun",
    "watering_frequency": 2,
    "growth_rate": "Medium",
    "maintenance_level": "Moderate",
    "plant_description": "Bell Peppers are colorful and sweet-tasting vegetables commonly used in cooking.",
    "image": "https://images.unsplash.com/photo-160448894382,5-f95dc6796ca5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8NHx8QmVsbCUyMFBlcHBlciUyMHBsYW50fGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 28,
    "common_name": "Zucchini",
    "scientific_name": "Cucurbita pepo",
    "other_name": "",
    "light_level": "full sun",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "High",
    "plant_description": "Zucchini is a summer squash with a mild flavor, often used in various culinary dishes.",
    "image": "https://images.pexels.com/photos/4750379/pexels-photo-4750379.jpeg?auto=compress&cs=tinysrgb&w=600"
  },
  {
    "plant_id": 29,
    "common_name": "Spinach",
    "scientific_name": "Spinacia oleracea",
    "other_name": "",
    "light_level": "partial shade",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "Moderate",
    "plant_description": "Spinach is a nutritious leafy green vegetable commonly used in salads and cooked dishes.",
    "image": "https://images.unsplash.com/photo-1576045057995-568f588f82,fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8Mnx8c3BpbmFjaHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=12,00&q=60"
  },
  {
    "plant_id": 30,
    "common_name": "Cherry Tomato",
    "scientific_name": "Solanum lycopersicum var. cerasiforme",
    "other_name": "",
    "light_level": "full sun",
    "watering_frequency": 2,
    "growth_rate": "Fast",
    "maintenance_level": "High",
    "plant_description": "Cherry Tomatoes are small, sweet tomatoes often used in salads and snacks.",
    "image": "https://images.unsplash.com/photo-1471194402,52,9-8e0f5a675de6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2,h8NHx8Q2,hlcnJ5JTIwVG9tYXRvfGVufDB8fDB8fHww&auto=format&fit=crop&w=12,00&q=60"
  }
]