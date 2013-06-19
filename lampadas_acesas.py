# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def lampadas_acesas(quantidade):
	
	lampadas = [False for i in range (quantidade)]
	for passada in range(quantidade): #passadas
		for i, lampada in enumerate(lampadas):
			if (i+1)%(passada + 1) == 0:
				lampadas[i] = not lampada

	return lampadas

class ProblemaParaResolverTest(unittest.TestCase):
    def teste_3_lampadas(self):
        self.assertEqual([True, False, False], lampadas_acesas(3))

    def teste_2_lampadas(self):
    	self.assertEqual([True, False], lampadas_acesas(2))

    def teste_4_lampadas(self):
    	self.assertEqual([True, False, False, True], lampadas_acesas(4))

    def teste_5_lampadas(self):
    	self.assertEqual([True, False, False, True, False], lampadas_acesas(5))

    def teste_6_lampadas(self):
    	self.assertEqual([True, False, False, True, False, False], lampadas_acesas(6))
if __name__ == '__main__':
    unittest.main()