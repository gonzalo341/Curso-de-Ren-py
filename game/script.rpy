# Personajes:

define a = Character("Alex", color="#00ff00")
define l = Character("Luna", color="#00bfff")
define r = Character("Rai", color="#ff6347")
define v = Character("Viktor", color="#ffffff")

#Inicio del juego.

label start:
    # Introducción
    scene bg labyrinth

    a "¿Dónde estoy? No recuerdo nada..."
    l "Parece que hemos caído en un extraño laberinto, Alex."
    r "¡Sí! Pero no sé cómo saldremos de aquí..."

    # El primer encuentro con Viktor
    v "Oh, parece que tenemos visitantes perdidos. Bienvenidos al Laberinto del Olvido."
    v "Soy Viktor, el conejo sabio, y los guiaré a través de este lugar. No se preocupen, todo tiene solución... si siguen mis consejos."

    menu:
        "Seguir a Viktor de inmediato":
            jump follow_viktor
        "Desconfiar de Viktor":
            jump distrust_viktor

label follow_viktor:
    # El protagonista sigue a Viktor y confía en él
    v "Perfecto, sigan mis pasos, y nada saldrá mal. Solo recuerden... seguir mis instrucciones."

    menu:
        "Ir por el camino de la izquierda":
            jump left_path
        "Ir por el camino de la derecha":
            jump right_path

label left_path:
    a "Creo que este camino se ve más seguro, vamos por aquí."
    l "¿Estás seguro, Alex? Algo no me gusta de esto..."

    v "¿No ven que todo está bien? Confíen en mí."

    # Descripción del camino izquierdo, que lleva a un final malo
    scene bg trap
    a "¡Ahhh! ¡Es una trampa!"

    v "Sabía que caerían en ella... Este es su destino."

    menu:
        "Seguir luchando":
            jump final_bad
        "Rendirse":
            jump final_bad

label right_path:
    a "Este camino parece más largo, pero siento que es el correcto."
    r "¡Vamos, no hay tiempo que perder!"

    v "Mmm... ¿Están seguros de esto? Este camino podría no ser tan fácil."

    # El camino correcto pero con complicaciones
    scene bg confusion
    a "Estoy empezando a ver sombras... ¿Qué está pasando aquí?"
    v "Nada de esto es real... todo es solo parte del juego."

    menu:
        "Luchar contra las sombras":
            jump fight_shadows
        "Seguir el camino sin luchar":
            jump final_good

label distrust_viktor:
    # El protagonista desconfía de Viktor
    a "No sé si puedo confiar en este conejo. Algo en él no me da buena espina."
    l "Tienes razón, Alex. Debemos averiguar más por nuestra cuenta."

    menu:
        "Buscar otra salida":
            jump search_exit
        "Pedir ayuda a Viktor":
            jump ask_viktor

label search_exit:
    # Buscar otra salida lleva a un final medio
    scene bg dead_end
    a "Este camino nos ha llevado a un callejón sin salida..."
    l "Parece que nos hemos equivocado, Alex. No queda más que seguir adelante."

    menu:
        "Intentar encontrar otro camino":
            jump final_neutral
        "Rendirse y esperar ayuda":
            jump final_neutral

label ask_viktor:
    # Pedir ayuda a Viktor lleva a la traición
    v "¿Buscan ayuda? Yo tengo lo que necesitan... solo sigan mis instrucciones."

    scene bg trap
    v "Ya lo dije, esto es lo que tenía planeado. Bienvenidos al final de su viaje."

    menu:
        "Luchar contra Viktor":
            jump final_bad
        "Aceptar su destino":
            jump final_bad

label fight_shadows:
    # Luchar contra las sombras lleva a un final bueno
    scene bg victory
    a "¡Lo logramos! ¡Hemos vencido a las sombras!"

    v "¿Cómo es posible? Este no era el camino que esperaba."

    menu:
        "Seguir adelante":
            jump final_good
        "Pedirle a Viktor más ayuda":
            jump final_good

label final_bad:
    # Final malo: el protagonista es atrapado
    scene bg black
    a "Todo se acaba aquí... hemos perdido."

    "El laberinto los ha atrapado para siempre."

    return

label final_good:
    # Final bueno: el protagonista logra escapar
    scene bg sunset
    a "Finalmente, después de tanto esfuerzo, encontramos la salida."

    "Alex, Luna, y Rai escapan del laberinto, dejando atrás las manipulaciones de Viktor."

    return

label final_neutral:
    # Final neutral: el protagonista sigue perdido
    scene bg gray
    a "Aunque no hemos escapado, al menos hemos llegado a un acuerdo con el laberinto."

    "Alex y los demás continúan vagando, pero ahora con una mayor comprensión del lugar."

    return
