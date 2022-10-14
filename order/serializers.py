from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields= ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields= '__all__'

    def create(self, validated_data):
        products = validated_data.pop('products')
        request = self.context['request']
        user = request.user
        order = Order.objects.create(user=user, status='open')
        for product in products:
            try:
                OrderItem.objects.create(order=order,
                                            product=product['product'],
                                            quantity=product['quantity'],)
            except KeyError:
                OrderItem.objects.create(order=order,
                                            product=product['product'],)
        return order