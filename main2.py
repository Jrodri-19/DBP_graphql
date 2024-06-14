from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# Definición del esquema
type_defs = gql("""
    type Query {
        products: [Product!]!
    }

    type Product {
        id: ID!
        name: String!
        price: Float!
    }
""")

# Datos de ejemplo
products_data = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Tablet", "price": 399.99},
]

# Definición de resolutores
query = QueryType()
product = ObjectType("Product")

@query.field("products")
def resolve_products(_, info):
    return products_data

# Construcción del esquema
schema = make_executable_schema(type_defs, query, product)

# Configuración del servidor GraphQL
app = GraphQL(schema, debug=True)
