"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from graphene_django.utils.testing import GraphQLTestCase
from seed.util.test_util import fill_test_database
from rest_auth.models import TokenModel
from app.models import User

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.headers = {"HTTP_AUTHORIZATION": 'Token ' + token.key}
    
    def test_query_carts(self):
        response_01 = self.query(
            '''
            {
                carts(query: "id=1", orderBy: "id", limit: 1){
                    id
                    buyer {
                      id
                    }
                    payment {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["carts"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                carts{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["carts"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                cartPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    carts { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["cartPagination"]["totalPages"], 1)
            self.assertEqual(res_03["cartPagination"]["totalCount"], 1)
            self.assertEqual(res_03["cartPagination"]["carts"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                cartCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["cartCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                cartCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["cartCount"]["count"], 1)

    def test_query_cart(self):
        response = self.query(
            '''
            {
                cart(id: 1){
                    id
                    buyer {
                      id
                    }
                    payment {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["cart"]["id"], 1)
    
    def test_save_cart(self):
        response = self.query(
            '''
            mutation {
                saveCart(
                    buyer:  1,
                    payment:  1,
                ) {
                    cart {
                        id
                        buyer {
                          id
                        }
                        payment {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveCart"]["cart"]["id"], 2)
    
    def test_set_cart(self):
        response = self.query(
            '''
            mutation {
                setCart(id:1
                    buyer:  1,
                    payment:  1,

                ) {
                    cart {
                        id
                        buyer {
                          id
                        }
                        payment {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setCart"]["cart"]["id"], 1)
    
    def test_delete_cart(self):
        response = self.query(
            '''
            mutation {
                deleteCart(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteCart"]["id"], 1)

    def test_query_categories(self):
        response_01 = self.query(
            '''
            {
                categories(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["categories"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                categories{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["categories"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                categoryPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    categories { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["categoryPagination"]["totalPages"], 1)
            self.assertEqual(res_03["categoryPagination"]["totalCount"], 1)
            self.assertEqual(res_03["categoryPagination"]["categories"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                categoryCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["categoryCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                categoryCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["categoryCount"]["count"], 1)

    def test_query_category(self):
        response = self.query(
            '''
            {
                category(id: 1){
                    id
                    name
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["category"]["id"], 1)
    
    def test_save_category(self):
        response = self.query(
            '''
            mutation {
                saveCategory(
                    name: "",
                ) {
                    category {
                        id
                        name
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveCategory"]["category"]["id"], 2)
    
    def test_set_category(self):
        response = self.query(
            '''
            mutation {
                setCategory(id:1
                    name: "",

                ) {
                    category {
                        id
                        name
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setCategory"]["category"]["id"], 1)
    
    def test_delete_category(self):
        response = self.query(
            '''
            mutation {
                deleteCategory(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteCategory"]["id"], 1)

    def test_query_companies(self):
        response_01 = self.query(
            '''
            {
                companies(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    commonName
                    rfc
                    address
                    phone
                    email
                    active
                    photo {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["companies"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                companies{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["companies"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                companyPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    companies { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["companyPagination"]["totalPages"], 1)
            self.assertEqual(res_03["companyPagination"]["totalCount"], 1)
            self.assertEqual(res_03["companyPagination"]["companies"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                companyCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["companyCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                companyCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["companyCount"]["count"], 1)

    def test_query_company(self):
        response = self.query(
            '''
            {
                company(id: 1){
                    id
                    name
                    commonName
                    rfc
                    address
                    phone
                    email
                    active
                    photo {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["company"]["id"], 1)
    
    def test_save_company(self):
        response = self.query(
            '''
            mutation {
                saveCompany(
                    name: "",
                    commonName: "",
                    rfc: "",
                    address: "",
                    phone: "",
                    email: "",
                    active: false,
                    photo: 1,
                ) {
                    company {
                        id
                        name
                        commonName
                        rfc
                        address
                        phone
                        email
                        active
                        photo {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveCompany"]["company"]["id"], 2)
    
    def test_set_company(self):
        response = self.query(
            '''
            mutation {
                setCompany(id:1
                    name: "",
                    commonName: "",
                    rfc: "",
                    address: "",
                    phone: "",
                    email: "",
                    active: false,
                    photo: 1,

                ) {
                    company {
                        id
                        name
                        commonName
                        rfc
                        address
                        phone
                        email
                        active
                        photo {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setCompany"]["company"]["id"], 1)
    
    def test_delete_company(self):
        response = self.query(
            '''
            mutation {
                deleteCompany(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteCompany"]["id"], 1)

    def test_query_messages(self):
        response_01 = self.query(
            '''
            {
                messages(query: "id=1", orderBy: "id", limit: 1){
                    id
                    content
                    sender {
                      id
                    }
                    target {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["messages"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                messages{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["messages"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                messagePagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    messages { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["messagePagination"]["totalPages"], 1)
            self.assertEqual(res_03["messagePagination"]["totalCount"], 1)
            self.assertEqual(res_03["messagePagination"]["messages"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                messageCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["messageCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                messageCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["messageCount"]["count"], 1)

    def test_query_message(self):
        response = self.query(
            '''
            {
                message(id: 1){
                    id
                    content
                    sender {
                      id
                    }
                    target {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["message"]["id"], 1)
    
    def test_save_message(self):
        response = self.query(
            '''
            mutation {
                saveMessage(
                    content: "",
                    sender:  1,
                    target:  1,
                ) {
                    message {
                        id
                        content
                        sender {
                          id
                        }
                        target {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveMessage"]["message"]["id"], 2)
    
    def test_set_message(self):
        response = self.query(
            '''
            mutation {
                setMessage(id:1
                    content: "",
                    sender:  1,
                    target:  1,

                ) {
                    message {
                        id
                        content
                        sender {
                          id
                        }
                        target {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setMessage"]["message"]["id"], 1)
    
    def test_delete_message(self):
        response = self.query(
            '''
            mutation {
                deleteMessage(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteMessage"]["id"], 1)

    def test_query_opinions(self):
        response_01 = self.query(
            '''
            {
                opinions(query: "id=1", orderBy: "id", limit: 1){
                    id
                    title
                    description
                    rate
                    product {
                      id
                    }
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["opinions"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                opinions{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["opinions"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                opinionPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    opinions { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["opinionPagination"]["totalPages"], 1)
            self.assertEqual(res_03["opinionPagination"]["totalCount"], 1)
            self.assertEqual(res_03["opinionPagination"]["opinions"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                opinionCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["opinionCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                opinionCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["opinionCount"]["count"], 1)

    def test_query_opinion(self):
        response = self.query(
            '''
            {
                opinion(id: 1){
                    id
                    title
                    description
                    rate
                    product {
                      id
                    }
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["opinion"]["id"], 1)
    
    def test_save_opinion(self):
        response = self.query(
            '''
            mutation {
                saveOpinion(
                    title: "",
                    description: "",
                    rate: 128,
                    product:  1,
                    user:  1,
                ) {
                    opinion {
                        id
                        title
                        description
                        rate
                        product {
                          id
                        }
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveOpinion"]["opinion"]["id"], 2)
    
    def test_set_opinion(self):
        response = self.query(
            '''
            mutation {
                setOpinion(id:1
                    title: "",
                    description: "",
                    rate: 128,
                    product:  1,
                    user:  1,

                ) {
                    opinion {
                        id
                        title
                        description
                        rate
                        product {
                          id
                        }
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setOpinion"]["opinion"]["id"], 1)
    
    def test_delete_opinion(self):
        response = self.query(
            '''
            mutation {
                deleteOpinion(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteOpinion"]["id"], 1)

    def test_query_payments(self):
        response_01 = self.query(
            '''
            {
                payments(query: "id=1", orderBy: "id", limit: 1){
                    id
                    cardNumber
                    expireDate
                    type
                    address
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["payments"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                payments{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["payments"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                paymentPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    payments { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["paymentPagination"]["totalPages"], 1)
            self.assertEqual(res_03["paymentPagination"]["totalCount"], 1)
            self.assertEqual(res_03["paymentPagination"]["payments"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                paymentCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["paymentCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                paymentCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["paymentCount"]["count"], 1)

    def test_query_payment(self):
        response = self.query(
            '''
            {
                payment(id: 1){
                    id
                    cardNumber
                    expireDate
                    type
                    address
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["payment"]["id"], 1)
    
    def test_save_payment(self):
        response = self.query(
            '''
            mutation {
                savePayment(
                    cardNumber: "",
                    expireDate: "",
                    type: "DEBIT",
                    user:  1,
                    address: "",
                ) {
                    payment {
                        id
                        cardNumber
                        expireDate
                        type
                        address
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePayment"]["payment"]["id"], 2)
    
    def test_set_payment(self):
        response = self.query(
            '''
            mutation {
                setPayment(id:1
                    cardNumber: "",
                    expireDate: "",
                    type: "DEBIT",
                    user:  1,
                    address: "",

                ) {
                    payment {
                        id
                        cardNumber
                        expireDate
                        type
                        address
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPayment"]["payment"]["id"], 1)
    
    def test_delete_payment(self):
        response = self.query(
            '''
            mutation {
                deletePayment(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePayment"]["id"], 1)

    def test_query_products(self):
        response_01 = self.query(
            '''
            {
                products(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    shortDescription
                    description
                    user {
                      id
                    }
                    sales {
                      id
                    }
                    category {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["products"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                products{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["products"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                productPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    products { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["productPagination"]["totalPages"], 1)
            self.assertEqual(res_03["productPagination"]["totalCount"], 1)
            self.assertEqual(res_03["productPagination"]["products"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                productCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["productCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                productCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["productCount"]["count"], 1)

    def test_query_product(self):
        response = self.query(
            '''
            {
                product(id: 1){
                    id
                    name
                    shortDescription
                    description
                    user {
                      id
                    }
                    sales {
                      id
                    }
                    category {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["product"]["id"], 1)
    
    def test_save_product(self):
        response = self.query(
            '''
            mutation {
                saveProduct(
                    name: "",
                    shortDescription: "",
                    description: "",
                    user:  1,
                    sales:  1,
                    category:  1,
                ) {
                    product {
                        id
                        name
                        shortDescription
                        description
                        user {
                          id
                        }
                        sales {
                          id
                        }
                        category {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveProduct"]["product"]["id"], 2)
    
    def test_set_product(self):
        response = self.query(
            '''
            mutation {
                setProduct(id:1
                    name: "",
                    shortDescription: "",
                    description: "",
                    user:  1,
                    sales:  1,
                    category:  1,

                ) {
                    product {
                        id
                        name
                        shortDescription
                        description
                        user {
                          id
                        }
                        sales {
                          id
                        }
                        category {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setProduct"]["product"]["id"], 1)
    
    def test_delete_product(self):
        response = self.query(
            '''
            mutation {
                deleteProduct(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteProduct"]["id"], 1)

    def test_query_purchases(self):
        response_01 = self.query(
            '''
            {
                purchases(query: "id=1", orderBy: "id", limit: 1){
                    id
                    amount
                    product
                    sale
                    shipping {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["purchases"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                purchases{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["purchases"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                purchasePagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    purchases { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["purchasePagination"]["totalPages"], 1)
            self.assertEqual(res_03["purchasePagination"]["totalCount"], 1)
            self.assertEqual(res_03["purchasePagination"]["purchases"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                purchaseCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["purchaseCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                purchaseCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["purchaseCount"]["count"], 1)

    def test_query_purchase(self):
        response = self.query(
            '''
            {
                purchase(id: 1){
                    id
                    amount
                    product
                    sale
                    shipping {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["purchase"]["id"], 1)
    
    def test_save_purchase(self):
        response = self.query(
            '''
            mutation {
                savePurchase(
                    amount: 128,
                    product: "{}",
                    sale: "{}",
                    shipping:  1,
                ) {
                    purchase {
                        id
                        amount
                        product
                        sale
                        shipping {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePurchase"]["purchase"]["id"], 2)
    
    def test_set_purchase(self):
        response = self.query(
            '''
            mutation {
                setPurchase(id:1
                    amount: 128,
                    product: "{}",
                    sale: "{}",
                    shipping:  1,

                ) {
                    purchase {
                        id
                        amount
                        product
                        sale
                        shipping {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPurchase"]["purchase"]["id"], 1)
    
    def test_delete_purchase(self):
        response = self.query(
            '''
            mutation {
                deletePurchase(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePurchase"]["id"], 1)

    def test_query_sales(self):
        response_01 = self.query(
            '''
            {
                sales(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    disscount
                    startDate
                    endDate
                    user {
                      id
                    }
                    banner {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["sales"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                sales{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["sales"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                salePagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    sales { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["salePagination"]["totalPages"], 1)
            self.assertEqual(res_03["salePagination"]["totalCount"], 1)
            self.assertEqual(res_03["salePagination"]["sales"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                saleCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["saleCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                saleCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["saleCount"]["count"], 1)

    def test_query_sale(self):
        response = self.query(
            '''
            {
                sale(id: 1){
                    id
                    name
                    disscount
                    startDate
                    endDate
                    user {
                      id
                    }
                    banner {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["sale"]["id"], 1)
    
    def test_save_sale(self):
        response = self.query(
            '''
            mutation {
                saveSale(
                    name: "",
                    disscount: 128.0,
                    startDate: "2020-01-01T12:00:00+00:00",
                    endDate: "2020-01-01T12:00:00+00:00",
                    user:  1,
                    banner: 1,
                ) {
                    sale {
                        id
                        name
                        disscount
                        startDate
                        endDate
                        user {
                          id
                        }
                        banner {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveSale"]["sale"]["id"], 2)
    
    def test_set_sale(self):
        response = self.query(
            '''
            mutation {
                setSale(id:1
                    name: "",
                    disscount: 128.0,
                    startDate: "2020-01-01T12:00:00+00:00",
                    endDate: "2020-01-01T12:00:00+00:00",
                    user:  1,
                    banner: 1,

                ) {
                    sale {
                        id
                        name
                        disscount
                        startDate
                        endDate
                        user {
                          id
                        }
                        banner {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setSale"]["sale"]["id"], 1)
    
    def test_delete_sale(self):
        response = self.query(
            '''
            mutation {
                deleteSale(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteSale"]["id"], 1)

    def test_query_shippings(self):
        response_01 = self.query(
            '''
            {
                shippings(query: "id=1", orderBy: "id", limit: 1){
                    id
                    info
                    folio
                    address
                    status
                    seller {
                      id
                    }
                    cart {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["shippings"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                shippings{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["shippings"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                shippingPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    shippings { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["shippingPagination"]["totalPages"], 1)
            self.assertEqual(res_03["shippingPagination"]["totalCount"], 1)
            self.assertEqual(res_03["shippingPagination"]["shippings"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                shippingCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["shippingCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                shippingCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["shippingCount"]["count"], 1)

    def test_query_shipping(self):
        response = self.query(
            '''
            {
                shipping(id: 1){
                    id
                    info
                    folio
                    address
                    status
                    seller {
                      id
                    }
                    cart {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["shipping"]["id"], 1)
    
    def test_save_shipping(self):
        response = self.query(
            '''
            mutation {
                saveShipping(
                    info: "",
                    folio: "",
                    address: "",
                    status: "CREATED",
                    seller:  1,
                    cart:  1,
                ) {
                    shipping {
                        id
                        info
                        folio
                        address
                        status
                        seller {
                          id
                        }
                        cart {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveShipping"]["shipping"]["id"], 2)
    
    def test_set_shipping(self):
        response = self.query(
            '''
            mutation {
                setShipping(id:1
                    info: "",
                    folio: "",
                    address: "",
                    status: "CREATED",
                    seller:  1,
                    cart:  1,

                ) {
                    shipping {
                        id
                        info
                        folio
                        address
                        status
                        seller {
                          id
                        }
                        cart {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setShipping"]["shipping"]["id"], 1)
    
    def test_delete_shipping(self):
        response = self.query(
            '''
            mutation {
                deleteShipping(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteShipping"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    address
                    active
                    type
                    photo {
                      id
                    }
                    company {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    address
                    active
                    type
                    photo {
                      id
                    }
                    company {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    address: "",
                    active: false,
                    type: "SUPERADMIN",
                    photo: 1,
                    company:  1,
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        address
                        active
                        type
                        photo {
                          id
                        }
                        company {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    address: "",
                    active: false,
                    type: "SUPERADMIN",
                    photo: 1,
                    company:  1,

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        address
                        active
                        type
                        photo {
                          id
                        }
                        company {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)

    def test_query_variants(self):
        response_01 = self.query(
            '''
            {
                variants(query: "id=1", orderBy: "id", limit: 1){
                    id
                    price
                    stock
                    shipment
                    product {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["variants"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                variants{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["variants"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                variantPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    variants { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["variantPagination"]["totalPages"], 1)
            self.assertEqual(res_03["variantPagination"]["totalCount"], 1)
            self.assertEqual(res_03["variantPagination"]["variants"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                variantCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["variantCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                variantCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["variantCount"]["count"], 1)

    def test_query_variant(self):
        response = self.query(
            '''
            {
                variant(id: 1){
                    id
                    price
                    stock
                    shipment
                    product {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["variant"]["id"], 1)
    
    def test_save_variant(self):
        response = self.query(
            '''
            mutation {
                saveVariant(
                    product:  1,
                    price: 128.0,
                    stock: 128,
                    shipment: 128.0,
                ) {
                    variant {
                        id
                        price
                        stock
                        shipment
                        product {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveVariant"]["variant"]["id"], 2)
    
    def test_set_variant(self):
        response = self.query(
            '''
            mutation {
                setVariant(id:1
                    product:  1,
                    price: 128.0,
                    stock: 128,
                    shipment: 128.0,

                ) {
                    variant {
                        id
                        price
                        stock
                        shipment
                        product {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setVariant"]["variant"]["id"], 1)
    
    def test_delete_variant(self):
        response = self.query(
            '''
            mutation {
                deleteVariant(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteVariant"]["id"], 1)

    def test_query_variantoptions(self):
        response_01 = self.query(
            '''
            {
                variantoptions(query: "id=1", orderBy: "id", limit: 1){
                    id
                    title
                    value
                    variant {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["variantoptions"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                variantoptions{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["variantoptions"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                variantoptionPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    variantoptions { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["variantoptionPagination"]["totalPages"], 1)
            self.assertEqual(res_03["variantoptionPagination"]["totalCount"], 1)
            self.assertEqual(res_03["variantoptionPagination"]["variantoptions"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                variantoptionCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["variantoptionCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                variantoptionCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["variantoptionCount"]["count"], 1)

    def test_query_variantoption(self):
        response = self.query(
            '''
            {
                variantoption(id: 1){
                    id
                    title
                    value
                    variant {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["variantoption"]["id"], 1)
    
    def test_save_variantoption(self):
        response = self.query(
            '''
            mutation {
                saveVariantoption(
                    title: "",
                    value: "",
                    variant:  1,
                ) {
                    variantoption {
                        id
                        title
                        value
                        variant {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveVariantoption"]["variantoption"]["id"], 2)
    
    def test_set_variantoption(self):
        response = self.query(
            '''
            mutation {
                setVariantoption(id:1
                    title: "",
                    value: "",
                    variant:  1,

                ) {
                    variantoption {
                        id
                        title
                        value
                        variant {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setVariantoption"]["variantoption"]["id"], 1)
    
    def test_delete_variantoption(self):
        response = self.query(
            '''
            mutation {
                deleteVariantoption(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteVariantoption"]["id"], 1)