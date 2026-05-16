import os
import kagglehub
import shutil

os.environ["KAGGLE_API_TOKEN"] = "KGAT_cb171658500eda32992810379c9fd969"

def iniciar_extracao():
    print(f"Iniciando extração da base Olist...")
    caminho_arquivos = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

    pasta_destino = "dados_brutos"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for arquivo in os.listdir(caminho_arquivos):
        caminho_completo_dados = os.path.join(caminho_arquivos, arquivo)
        caminho_completo_destino = os.path.join(pasta_destino, arquivo)
        if os.path.isfile(caminho_completo_dados):
            shutil.copy(caminho_completo_dados, caminho_completo_destino)
            print(f"Copiado: {arquivo}")    
    
    print(f"Sucesso! Tabelas baixadas em: {caminho_arquivos}")
    return caminho_arquivos

if __name__ == "__main__":    
    iniciar_extracao()    