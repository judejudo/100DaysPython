
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_notification(self,client,flight_price, dep_city_name,depature_iata_code, arrival_city_name,arrival_iata_code,outbound_date,inbound_date):
        message = client.messages.create(
            from_='+12564488119',
            body=f"Low price alert from Judosoft! Only £{flight_price} to fly from {dep_city_name}-{depature_iata_code} to {arrival_city_name}-{arrival_iata_code}, from {outbound_date} to {inbound_date}",
            to='+254797437715'
        )
        return message