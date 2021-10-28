from customers import customers
def return_inputs():
    while True:
        str_input=input("Please enter name and number of bills (A750, B15, Savaş100):")
        list_input_name=""
        list_input_bills=""
        temporary_i=0
        for i in range(0,len(str_input),1):
            if(str_input[i] not in ["1","2","3","4","5","6","7","8","9"]):
                list_input_name+=str_input[i]
            else:
                temporary_i=i
                break
        if (list_input_name == ""):
            print("Misspelling! Please try again.")
            continue
        for i in range(temporary_i,len(str_input),1):
            list_input_bills+=str_input[i]
        try:
            int_list_input_bills=int(list_input_bills)
            return list_input_name, int_list_input_bills
        except:
            print("Misspelling! Please try again.")
def return_index_function(number,list):
    list_index = -1
    for object in range(len(list)):
        if (list[object].number_of_bills == number):
            list_index = object
    return_index = list_index
    return return_index
def return_wanted_index(customer_parameter,customers_list_parameter):
    for i in range(len(customers_list_parameter)- 1, -1, -1):
        if (customers_list_parameter[i].number_of_bills > customer_parameter.number_of_bills and customers_list_parameter[i].max_delay + customer_parameter.number_of_bills <= customers_list_parameter[i].number_of_bills and i != 0):
            continue
        elif (i == 0 and customers_list_parameter[i].number_of_bills > customer_parameter.number_of_bills):
            wanted_index = 0
            return wanted_index
        elif (i == 0 and customers_list_parameter[i].number_of_bills <= customer_parameter.number_of_bills):
            wanted_index = 1
            return wanted_index
        else:
            if (customers_list_parameter[i].max_delay + customer_parameter.number_of_bills <= customers_list_parameter[i].number_of_bills and customers_list_parameter[i].number_of_bills > customer_parameter.number_of_bills):##Bulunan yerin önüne girer.
                wanted_index = i
                return wanted_index
            elif (customers_list_parameter[i].number_of_bills <= customer_parameter.number_of_bills):##Bulunan yerin arkasına girer.
                wanted_index = i + 1
                return wanted_index
            else:##Dolan yerlerden çıkabilecek en büyüğü çıkarıp yer açtıktan sonra küçüğü yerleştirir.
                sorted_number_of_bills = sorted(customers_list_parameter[:i],key=lambda index: (-index.number_of_bills, -index.customer_queue))##Kuyrukta önlerden çıkarırken en iyi verim için elemanlar fatura sayılarına göre büyükten küçüğe sıralanır.
                if (sorted_number_of_bills[0].number_of_bills <= customer_parameter.number_of_bills):##Gelen müşterinin fatura sayısı sıralılarında en büyüğünden büyükse öne giremez.
                    wanted_index = i + 1
                    return wanted_index
                counter = i
                wanted_index_bool=False
                for j in range(0, counter, 1):
                    for k in range(counter, len(customers_list_parameter), 1):
                        if (sorted_number_of_bills[j].customer_queue > customers_list_parameter[k].customer_queue and sorted_number_of_bills[j].number_of_bills>=customer_parameter.number_of_bills+sorted_number_of_bills[j].max_delay):
                            wanted_number=sorted_number_of_bills[j].number_of_bills##Değişecek müşterinin fatura sayısıdır.
                            insert_index=return_index_function(wanted_number,customers_list_parameter)##Değişecek müşterinin listede bulunduğu index için return_index_function fonksiyonu çağırılır.
                            temporary_identifier = customers_list_parameter[insert_index].max_delay
                            back_index_bool=False
                            for t in range(insert_index,k,1):##Müşterinin arkaya atılıp atılamayacağı kontrol edilir.
                                if (customers_list_parameter[insert_index].customer_queue < customers_list_parameter[t].customer_queue):
                                    temporary_identifier+=customers_list_parameter[t].number_of_bills
                                if(temporary_identifier>customers_list_parameter[insert_index].number_of_bills):
                                    back_index_bool=True
                                    break
                            if(back_index_bool==True):##Eğer atılamıyorsa bir sonraki müşteriye bakılır.
                                break
                            wanted_index_bool=True
                            customers_list_parameter.insert(k + 1, customers_list_parameter[insert_index])
                            for t in range(insert_index,k+1,1):
                                if (customers_list_parameter[insert_index].customer_queue > customers_list_parameter[t].customer_queue):##Arkaya atılan müşterinin önceden önüne geçtiklerinin ekstra bekleme süresi düşürülür.
                                    customers_list_parameter[t].max_delay -= customers_list_parameter[insert_index].number_of_bills
                            customers_list_parameter.remove(customers_list_parameter[insert_index])
                            return_wanted_index(customer_parameter, customers_list_parameter[:insert_index])##Eklenen müşteri kuyrukta daha öne gidebiliyor mu bakmak için klendiği yerin önündekiler ile fonksiyon yeniden çağırılır.
                            break
                        elif(sorted_number_of_bills[j].number_of_bills > customers_list_parameter[k].number_of_bills):
                            break
                    if (wanted_index_bool == True):
                        break
                if(wanted_index_bool==False):##for döngüsünde önden alınacak eleman bulunamazsa yeni eleman i+1 indeksine girer.
                    wanted_index=i+1
                    return wanted_index
def print_customers(list):
    print("Server <---",end=' ')
    for customer_in_list in list:
        str_number=str(customer_in_list.number_of_bills)
        str_name=customer_in_list.customers_name
        print(str_name+str_number,end=' ')
    print(" ")
another_customer="y"
customers_list=[]
last_customer=customers()
number_of_customers=0
while(another_customer in ["Y","y","Yes","yes"]):
    customer_name,customer_bills = return_inputs()
    customer=customers(customer_name,customer_bills,number_of_customers+1)
    if(len(customers_list)==0):##başa ekleme
        customers_list.append(customer)
        number_of_customers+= 1
        last_customer=customer
    elif(last_customer.number_of_bills<=customer.number_of_bills):##sona ekleme
        customers_list.append(customer)
        number_of_customers+=1
        last_customer=customer
    else:##aralara ekleme
        wanted_index=return_wanted_index(customer,customers_list)
        customers_list.insert(wanted_index, customer)
        for i in range(wanted_index+1,len(customers_list),1):##müşteri öne alındıktan sonra arkasındakilerin ekstra bekleme süresi arttırılır.
            customers_list[i].max_delay += customer.number_of_bills
        number_of_customers+=1
    print_customers(customers_list)
    another_customer = input("Are there any other customer? (Y,y,Yes,yes,N,n,No,no) ")
    while(another_customer not in ["Y","y","Yes","yes","N","n","No","no"]):
        print("Misspelling!")
        another_customer = input("Are there any other customer? (Y,y,Yes,yes,N,n,No,no) ")
