class customers:
    def __init__(self,customers_name="NaN",number_of_bills=0,customer_queue=0,max_delay=0):
        self.customers_name=customers_name
        self.number_of_bills=number_of_bills
        self.customer_queue = customer_queue##Müşterinin kaçıncı sırada geldiği burada bulunur.
        self.max_delay=max_delay##Müşterinin ekstra bekleme süresi burada bulunur.