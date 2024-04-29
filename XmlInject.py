import argparse
import xml.etree.ElementTree as ET

# Função que converte um XML em código de ligação no formato desejado
def convert_xml_to_binding_code(xml_path):
    # Carregar o XML do arquivo especificado
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Lista para armazenar o código de ligação gerado
    binding_code = []

    # Itere sobre cada elemento <bind>
    for bind in root.findall('bind'):
        # Obtenha os valores de "service", "to", e "name"
        service = bind.get('service')
        to = bind.get('to')
        name = bind.get('name', 'default')  # Padrão para 'default'

        # Extrai a parte relevante do nome do serviço e do 'to'
        service_short = service.split(',')[0]
        to_short = to.split(',')[0]

        # Crie a linha de código no formato desejado
        binding_code.append(f"this.Bind<{service_short}>().To<{to_short}>().Named('{name}');")

    return binding_code

# Função principal para ler o caminho do arquivo e salvar o resultado em um arquivo de texto
def main():
    # Configurar o parser de argumentos para receber o caminho do arquivo XML
    parser = argparse.ArgumentParser(description="Transforma um arquivo XML em código de ligação.")
    parser.add_argument("xml_path", help="Caminho do arquivo XML de entrada.")
    parser.add_argument("output_path", help="Caminho do arquivo de saída para salvar o código gerado.")

    args = parser.parse_args()

    # Converter o XML em código de ligação
    binding_code = convert_xml_to_binding_code(args.xml_path)

    # Salvar o código gerado no arquivo de saída
    with open(args.output_path, 'w') as f:
        for code in binding_code:
            f.write(f"{code}\n")

    print(f"Código gerado e salvo em: {args.output_path}")

# Se o script está sendo executado diretamente, chama a função principal
if __name__ == "__main__":
    main()
