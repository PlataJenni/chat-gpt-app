```
NAME
       chatgpt-api.py

VERSION
        1.0
AUTHOR
	Hely Salgado 

DESCRIPTION

	interfaz CLI para chatgpt

	El programa es una interfaz para interaccionar con chatpgt
	usando el modelo gpt-3.5-turbo

	Hay dos opciones:
	new:  crear una nueva conversación con el chat
	exit: para salirse de la interfaz

CATEGORY
	chatbots

USAGE
	python chatgpt-api.py

ARGUMENTS

        none

SEE ALSO
 	tomado de : https://gist.github.com/mouredev/58abfbcef017efaf3852e8821564c011

```


##### librerias
importar  openai   # pip instalar openai
importar  configuración  # local
importar  typer   # pip install "typer[all]"
from  rich  import  print   # pip install rich
de  rico _ importar tabla  Tabla 

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Digitador: https://typer.tiangolo.com
- Rico: https://rich.readthedocs.io/en/stable/
"""


def  principal ():

    abierto _ api_key  =  config . Clave API

    print ( "💬 [negrita verde]ChatGPT API en Python[/negrita verde]" )

    tabla  =  Tabla ( "Comando" , "Descripción" )
    mesa _ add_row ( "salir" , "Salir de la aplicación" )
    mesa _ add_row ( "new" , "Crear una nueva conversación" )

    imprimir ( tabla )

    # Dando Contexto del asistente
    contexto  = { "rol" : "sistema" ,
               "content" : "Eres un asistente que sabe todo sobre k-pop" }
    mensajes  = [ contexto ]

    mientras que  es cierto :

        contenido  =  __prompt ()

        si  el contenido  ==  "nuevo" :
            print ( "🆕 Nueva conversacion creada" )
            mensajes  = [ Se cambio el contexto ]
            contenido  =  __prompt ()

        mensajes _ agregar ({ "rol" : "usuario" , "contenido" : contenido })

        respuesta  =  openai . Finalización de chat . crear (
            modelo = "gpt-3.5-turbo" , mensajes = mensajes )

        # una respuesta
        respuesta_contenido  =  respuesta . opciones [ 0 ]. mensaje _ contenido

        mensajes _ agregar ({ "función" : "asistente" , "contenido" : respuesta_contenido })

        print ( f"[negrita roja]> [/negrita roja] [roja] { respuesta_contenido } [/roja]" )


def  __prompt () ->  str :
    indicador  =  tipeador . prompt ( " \n ¿Sobre qué quieres hablar?" )

    si  mensaje  ==  "salir" :
        salir  =  tipeador . confirmar ( "✋ ¿Estás seguro?" )
        si  sale :
            print ( "👋 ¡Hasta luego!" )
            levantar  tipeador . Abortar ()

        devolver  __prompt ()

     mensaje de retorno


si  __nombre__  ==  "__principal__" :
    tipeador _ ejecutar ( principal )