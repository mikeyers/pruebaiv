
# -*- coding: utf-8 -*-
import unittest, json
from src import main



class testClientes(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_principal(self):

        response = self.app.get('/')
        data = json.loads(response.data.decode())
        #Comprobamos que la ruta devuelve el estado correcto
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        #comprobamos que se haya de vuelto el status = OK
        self.assertTrue(data['status'] == 'OK')

    def test_status(self):

        response = self.app.get('/status')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(data['status'] == 'OK')


    def test_mostrar(self):

        response = self.app.get('/mostrar')
        # Se comprueba que el código de estado sea 200
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        # Se comprueba que se devuelva contenido json
        self.assertTrue(response.content_type == 'application/json')

    def test_busquedaNombre(self):

        response = self.app.get('/clientes/<nombre>')
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(response.content_type == 'application/json')

    def test_busquedaEstado(self):
        response = self.app.get('/clientes/<estado>')
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(response.content_type == 'application/json')

    def test_busquedaDNI(self):
        response = self.app.get('/DNI/<DNI>')
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(response.content_type == 'application/json')

    def test_busquedaProvincia(self):
        response = self.app.get('/provincia/<provincia>')
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(response.content_type == 'application/json')

    def test_busquedaRobinson(self):
        response = self.app.get('/robinson/<DNI>')
        self.assertEqual(response.status_code, 200, "Codigo no esperado")
        self.assertTrue(response.content_type == 'application/json')

if __name__ == "__main__":
    unittest.main()
