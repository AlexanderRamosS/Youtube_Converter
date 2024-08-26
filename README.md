# YouTube to MP3/MP4 Converter

Este é um aplicativo desenvolvido em Python que permite converter vídeos do YouTube em arquivos MP3 ou MP4, com uma interface gráfica intuitiva e uma barra de progresso para monitorar o download.

## Funcionalidades

- Baixa vídeos do YouTube e converte para MP3 ou MP4.
- Interface gráfica desenvolvida com PyQt5.
- Barra de progresso para acompanhar o progresso do download.
- Suporte ao modo escuro na interface gráfica.

## Requisitos

- Python 3.6 ou superior
- Ambiente virtual configurado (`venv`)
- `yt-dlp`
- `PyQt5`
- Codec FFmpeg (necessário para conversão de vídeos)

## Instalação

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/AlexanderRamosS/Youtube_Converter
   cd Youtube_Converter
   
2. Ative o ambiente virtual:

   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate  # Para Windows
   
3. Instale as dependências necessárias(o arquivo esta dentro da venv):

   pip install -r requirements.txt

4. Instale o codec FFmpeg:

  Pela internet: Baixe o FFmpeg diretamente do site oficial FFmpeg.org e siga as instruções de instalação.

  Pelo Chocolatey (Windows): Se você estiver usando Windows e tem o Chocolatey instalado, pode instalar o FFmpeg executando o seguinte comando no terminal:
  
    choco install ffmpeg

  Caso você não tenha o Chocolatey instalado, apenas abra o Windows PowerShell como administrador e rode o comando:

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

  Após rodar, basta apenas ir confirmando tudo o que for solicitado e pronto!!!

## Uso

1. Execute o script principal:
   python main.py

2. Insira a URL do vídeo do YouTube que você deseja baixar.

3. Escolha o formato desejado (MP3 ou MP4) e o diretório onde o arquivo será salvo.

4. Clique no botão "Baixar e Converter" para iniciar o download. A barra de progresso mostrará o progresso do download.

## Executável Compilado

  Se você estiver usando a versão compilada do programa, certifique-se de que o FFmpeg está instalado no sistema, conforme as instruções acima. Sem o FFmpeg, o programa não conseguirá baixar os vídeos do YouTube.

## Contribuindo
  Se você quiser contribuir para este projeto, sinta-se à vontade para abrir um pull request ou uma issue. Toda ajuda é bem-vinda!







