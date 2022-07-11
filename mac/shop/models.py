from django.db import models


class Product(models.Model):
    # Automatically giving a unique id to our products
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subCategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    # Published Date
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contacts(models.Model):
    # Automatically giving a unique id to our products
     msg_id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=50, default="")
     email = models.CharField(max_length=254, default="")
     phone = models.CharField(max_length=50, default="")
     desc = models.CharField(max_length=1000, default="")

     def __str__(self):
        return str(self.msg_id) + " -> " + self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default='')

    def __str__(self):
        return str(self.order_id) + " -> " + self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(default="", max_length=5000)
    # if nothing is provided , then default value will be current timestamp
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)+" -> "+str(self.update_desc[0:10]) + "..."
