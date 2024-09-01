from supabase_client import connect_db
from firebase_manager import send_notification
from flask import Flask, request, jsonify

supabase = connect_db()
app = Flask(__name__)

# Lista para almacenar los datos de las peticiones
test = {
    "type": "info",
    "tittle": "Desde Flask",
    "message": "Desde Flask",
}
request_log = [test]

@app.route('/api/cenit/v1/notifications', methods=['POST'])
def webhook():
    try:
        # Obtener datos del webhook
        data = request.json
        print("Datos recibidos:", data)

        # Verificar el tipo de evento y procesar según corresponda
        if data.get("event_type") == "INSERT":
            print("Evento INSERT recibido:", data)
            new_notification = {
                "type": "info",
                "tittle": "Desde Flask",
                "message": "Desde Flask",
            }

            # Inserta los datos en la tabla 'notifications'
            response = supabase.table('notifications').insert(new_notification).execute()
            # Verifica la respuesta
            if response:
                print("Inserción exitosa:", response.data)
            else:
                print("Error al insertar:", response.error)

        # Responder a Supabase
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print("Error al procesar el webhook:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/requests', methods=['GET'])
def view_requests():
    # Generar una vista simple de las peticiones recibidas
    return '''
    <html>
    <head><title>Notificaciones</title></head>
    <body>
        <h1>Notificaciones</h1>
        <ul>
            {}
        </ul>
    </body>
    </html>
    '''.format(''.join(f'<li>{item}</li>' for item in request_log))


if __name__ == '__main__':
    app.run(port=5000, debug=True)


# url: str = os.getenv('SUPABASE_URL')
# key: str = os.getenv('SUPABASE_KEY')

# client = RealtimeClient(url, key)
# channel = client.channel('test-channel')


# # Definir la función de callback para manejar la suscripción
# def _on_subscribe(status: RealtimeSubscribeStates, err: Optional[Exception]):
#     if status == RealtimeSubscribeStates.SUBSCRIBED:
#         print('Connected!')
#     elif status == RealtimeSubscribeStates.CHANNEL_ERROR:
#         print(f'There was an error subscribing to channel: {err}')
#     elif status == RealtimeSubscribeStates.TIMED_OUT:
#         print('Realtime server did not respond in time.')
#     elif status == RealtimeSubscribeStates.CLOSED:
#         print('Realtime channel was unexpectedly closed.')


# # Función para manejar e imprimir el payload de inserciones
# def handle_insert(payload):
#     print("Nuevo registro insertado en la tabla notifications:")
#     for key, value in payload['new'].items():
#         print(f"{key}: {value}")


# # Función para limpiar canales al cerrar o si ocurre un error
# async def clean_up():
#     print("Cleaning up channels...")
#     # Crear un canal para limpiar
#     channel_to_remove = client.channel('some-channel-to-remove')
#     await channel_to_remove.subscribe()
#     await client.remove_channel(channel_to_remove)
#     print("Channels cleaned up successfully.")


# # Función principal asíncrona
# async def main():
    
#     channel = client.channel(
#         "presence-test",
#         {
#             "config": {
#                 "presence": {
#                     "key": ""
#                 }
#             }
#         }
#     )

#     channel.subscribe(
#         lambda status, err: status == RealtimeSubscribeStates.SUBSCRIBED
#         and print("Ready to receive database changes!")
#     )
        
#     # Suscribirse al canal
#     await channel.subscribe(_on_subscribe)
#     await channel.on_broadcast("INSERT", lambda payload: print(payload)).subscribe()
    
#     # Configurar la función callback para manejar los eventos de inserción en la tabla notifications
#     channel.on_postgres_changes(
#         event="INSERT",
#         schema="public",
#         table="notifications",
#         # callback=lambda payload: print("All inserts in notifications table: ", payload),
#         callback=handle_insert
#     )

#     print(client.get_channels())

#     # Mantener la conexión activa
#     try:
#         while True:
#             await asyncio.sleep(1)  # Evita un bucle demasiado ajustado que consuma CPU

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         await clean_up()

#     except KeyboardInterrupt:
#         print("Service is shutting down...")
#         await clean_up()
#     finally:
#         client.close()

# # Ejecutar la función principal en un loop de eventos
# if __name__ == "__main__":
#     asyncio.run(main())

# print('ejecutando...')
# response_proofs = supabase.table('vw_proofs_running_bridge').select('*', count='exact').execute()
# response_notifications = supabase.table('notifications').select('*', count='exact').eq('seen', False).execute()

# # tokens = ["fhonTw7MRra58G7_IXb9R0:APA91bH4xTrJYdWwEUnx9i3zSj9sBxgBSPZXc7c554BhBnzTQWTU9uQJuEPcP-tzJHsEuMZbPygy0yorByzwEAGr-mdZpZ-ILWqBfxucMaOfms4J4NveRWLeo-0k783KNaJSPl_lh-pj"]
# # send_notification("success", "cenit notification", tokens)

# # Verifica si la consulta fue exitosa
# if response_proofs.data:
#     proofs = response_proofs.data
#     count = response_proofs.count
    
#     # Extraer los tokens de firebase
#     firebase_tokens = [proof['firebase_token'] for proof in proofs if 'firebase_token' in proof]

#     print(f"Firebase Tokens: {firebase_tokens}")
#     print(f"Total de registros: {count}")

#     # Opcional: Envía una notificación si hay tokens disponibles
#     if firebase_tokens:
#         send_notification("success", "cenit notification", firebase_tokens)

# else:
#     print("No se encontraron registros o hubo un error en la consulta.")


# # # Verifica si la consulta fue exitosa
# # if response_notifications.data:
# #     notifications = response_notifications.data
# #     count = response_notifications.count
    
# #     print(notifications, count)

# # else:
# #     print("No se encontraron registros o hubo un error en la consulta.")
