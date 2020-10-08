from google_drive_downloader import GoogleDriveDownloader as gdd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import markdown2 as mkd2
import os



def dowloadImgPng(idpic, name, overwriteImgs=True):
    path = './imgs/{}_{}.png'.format(name, idpic)
    gdd.download_file_from_google_drive(file_id=idpic, dest_path=path,unzip=False, overwrite=overwriteImgs)
    return path


def getImageAsMarkdown(id, overwriteImgs=True):
    path = dowloadImgPng(id,'pic', overwriteImgs)
    return '![{}]({})'.format(path, path)

def run(filename, pagetitle = 'Documento de avaliação segundo as Heurísticas de Nielsen', subtitle = '', sheetname = 'Respostas - HeurNiel', sheetNum = 0, printrecords = False, printMarkdown = False, verbose=True, overwriteimgs = False):

    imagecount = 0

    if verbose:print('Connecting to google sheets... ')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # File name in google drive
    sheet = client.open(sheetname).get_worksheet(sheetNum)

    records = sheet.get_all_records()
    size = len(records)
    lineCount = 0
    if verbose: print('DONE.')
    if printrecords:pprint(records)

    output = {}
    problemCount = {}
    separatedOutput = {}

    if printrecords:pprint(records)

    if verbose: print('Generating file header... ')

    headerMd = '# {}\n'.format(pagetitle)
    headerMd += '## {}\n'.format(subtitle)
    headerMd += '**Página Avaliada**: [https://www.dac.unicamp.br/portal/acesso/estudantes](https://www.dac.unicamp.br/portal/acesso/estudantes)\n\n'
    headerMd += '\n![data/paginaavaliada.png](data/paginaavaliada.png)\n'
    headerMd += 'O procedimento de avaliação das heurísticas foi feito em dois momentos distintos. Primeiro, cada um dos quatro integrantes do grupo avaliou individualmente o site da Diretoria Acadêmica. Foi criado um documento no GOOGLE FORMS contendo cada uma das questões referentes aos problemas, tais como: nome,  seção onde o problema aparece, descrição do problema, imagem, heurísticas, justificativa e grau de severidade. O documento foi preenchido para cada problema individualmente, gerando um documento do Google Sheets como resultado. Esse documento foi processado por um programa escrito em Python para colocar os dados da tabela em um documento de texto.\n'
    headerMd += '\n'
    headerMd += 'Após a avaliação ter sido feita individualmente (os alunos não trocaram informações sobre os problemas encontrados durante o período de análise), o grupo se uniu para definir quais problemas em comum foram encontrados. Os problemas que foram encontrados individualmente foram avaliados, e alguns erros na definição de heurísticas e graus de severidade foram corrigidos.\n'
    headerMd += '\n\n**Formulário utilizado**\n'
    headerMd += '\n![data/form.png](data/form.png)\n\n\n'

    headerMd += '\n* **Link para o formulário utilizado**: [Formulário](https://docs.google.com/forms/d/e/1FAIpQLScmZ_LzhXA_dx5XmhWrQjtcYFNG7xgcjER1TXufxEPOvflIjQ/viewform)\n'
    headerMd += '* **Link para o software desenvolvido**: [GitHub](https://github.com/ALREstevam/Gsheet-IHC/)\n'



    #headerMd += '# Sumário'
    #headerMd += '\n[TOC]\n'
    headerMd += '\n---------------\n\n\n'
    if verbose: print('DONE.')


    for line in records:
        localMarkdown = ''
        markdownText = ''
        lineCount += 1

        group = line['Agrupar em']
        section = line['Seção onde o problema aparece']

        #Counts the problem for each author
        if line['Agrupar em'] in problemCount.keys():
            problemCount[group] += 1
        else:
            problemCount[group] = 1
        if verbose: print('>>> PROCESSING LINE... INFO: PROBLEM {:3} FOR {:20}\t--------------- [ {:3}/{:3} ] ------ {:3.2f}% ------ '.format(problemCount[group], line['Agrupar em'], lineCount, size, (lineCount * 100)/size))
        problid = generateId(line['Seção onde o problema aparece'], group ,problemCount[group])
        localMarkdown += '\n\n\n\n## *id:[{}]* Problema {}: {}\n'.format(problid, problemCount[group], line['Nome curto para o problema'])
        localMarkdown += '**Ocorre na página**: *{} > {}*\n\n'.format(str(line['Seção onde o problema aparece']).strip(), str(line['Seção onde o problema ocorre (ex: "Adicionar documentos")']).strip())

        if not str(line['Descrição do problema']).endswith('.'): line['Descrição do problema'] += '.'

        localMarkdown += line['Descrição do problema'] + '\n'

        localMarkdown += "## Fotos\n"

        fotos = str(line['Fotos (PNG)']).replace('\'','').split(',')

        #Downloads the pictures and generates the corresponding markdown for it
        for foto in fotos:
            imagecount += 1
            path = dowloadImgPng(foto.strip().replace('https://drive.google.com/open?id=',''), str(group).upper(), overwriteimgs)
            localMarkdown += '![{}]({})\n\n'.format(foto.strip(), path)

        #This is an optional fild that will be added olny if it has some text
        if line['Comentários'] != '':
            localMarkdown += "## Comentários\n"
            if not str(line['Comentários']).endswith('.'): line['Comentários'] += '.'
            localMarkdown += line['Comentários'] + '\n\n'

        localMarkdown += '## Considerações\n\n'
        localMarkdown += '### Heurística ferida: {}ª\n'.format(str(line['Heurística que fere']).split('.')[0])
        localMarkdown += '**Heurística ferida**: {}\n\n'.format(str(line['Heurística que fere']).split(' -')[0].replace('.', ' -'))
        if not str(line['Justificativa para a heurística']).endswith('.'): line['Justificativa para a heurística'] += '.'

        localMarkdown += '**Justificativa**: {}\n\n'.format(line['Justificativa para a heurística'])

        localMarkdown += '### Grau de Serveridade do problema\n'
        localMarkdown += '**Grau de Severidade**: {})\n\n'.format(str(line['Grau de severidade']).replace(' - ',' (').replace('.', ' -'))


        markdownText = localMarkdown
        # Groups avaliations of the same authon together
        if line['Agrupar em'] in output.keys():
            output[group] += markdownText
        else:
            output[group] = '# Problemas levantados por: *{}*\n'.format(group) + markdownText


        if group in separatedOutput.keys():
            #People exists
            if section in separatedOutput[group].keys():
                #Section exists
                separatedOutput[group][section] += markdownText
            else:
                #Section does not exists
                separatedOutput[group][section] = '# {}\n {}'.format(section, localMarkdown)
        else:
            #People and section does not exists
            print('Adding {} for {}'.format(section, group))
            separatedOutput[group] = {}
            separatedOutput[group][section] = '# {}\n {}'.format(section, localMarkdown)
    if printMarkdown: print('\n\n' + 20 * '-' + ' GENERATED MARKDOWN ' + 20 * '-' + '\n\n')
    #pprint(separatedOutput)




    resultMarkdown = ''
    if verbose: print('WRITING MARKDOWN FILE... ')
    # Writes the generated markdown to a .md file
    with open('{}.md'.format(filename), 'w', encoding='utf8') as file:
        file.write(headerMd)
        resultMarkdown += headerMd
        for key, personData in output.items():
            if printMarkdown:print(personData)
            file.write(personData + '\n')
            file.write('\n\n---------\n\n')
            resultMarkdown += personData + '\n\n---------\n\n'
            if verbose: print('WRITING {}...'.format(key))
    if verbose: print('DONE. ')

    if verbose: print('CONVERTING Makdown to html and WRITING TO A FILE...')
    # Converts the markdown to an html file

    htmlBegin = '<!DOCTYPE html>'\
                '<html lang="br">'\
                '<head>'\
                '    <meta charset="UTF-8">'\
                '    <title>Title</title>'\
                '    <style>'\
                '        *{'\
                '            font-family: "Open Sans", Calibri, SansSerif, sans-serif;'\
                '        }'\
                '        p{'\
                '            text-align: justify;'\
                '        }'\
                '        img{'\
                '            border: solid 1px #000000;'\
                '            display: block;'\
                '            margin-left: auto;'\
                '            margin-right: auto;'\
                '            width: 90%;'\
                '        }'\
                '    </style>'\
                '</head>'\
                '<body>'

    htmlEnd = '</body>\n' \
              '</html>\n'

    with open('{}.html'.format(filename), 'w', encoding='utf8') as file:
        file.write('{}\n{}\n{}\n'.format(htmlBegin, mkd2.markdown(resultMarkdown), htmlEnd))
    if verbose:print('DONE. ')

    if verbose: print('MAKING SEPARATED FILES...')
    for name, data in separatedOutput.items():
        for page, text in data.items():
            path = 'sep/{}'.format(page)
            if not os.path.exists(path.format()):
                os.makedirs(path)
            with open('{}/{}_{}.md'.format(path, page, name), 'w') as mdFile:
                with open('{}/{}_{}.html'.format(path, page, name), 'w', encoding='utf8') as htmlFile:

                    text = str(text).replace('./', '../../')

                    print('CREATING FILES:\t {:40} for \t{:10} ... '.format(page, name), end='')
                    mdFile.write(text)





                    htmlFile.write('{}\n{}\n{}'.format(htmlBegin, mkd2.markdown(text), htmlEnd))
                    print('\tDONE.')
    print('IMAGES: {}'.format(imagecount))









def generateId(areaname, personName, problemNumber):
    areaname = areaname.replace(' de ', ' ').replace(' da ', ' ').replace(' e ', ' ')
    areaname = str(areaname).upper()
    areaname = areaname.split(' -')[0]
    areaname = areaname.replace('Ê', 'E').replace('Ç', 'C').replace(' ','_').replace('Ã','A')
    areaname2 = []
    for character in areaname:
        if character in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _'.split(' '):
            areaname2 += character

    areaname = ''.join(areaname2)
    areaname = areaname.replace('SERVICOS', 'SRV')\
        .replace('SERVICO', 'SRV')\
        .replace('ACADEMICOS', 'ACADM')\
        .replace('ACADEMICO', 'ACADM')\
        .replace('SISTEMAS', 'SYS')\
        .replace('SISTEMA', 'SYS')


    areaname2 = areaname.split('_')
    areaname3 = []

    for elem in areaname2:
        if len(elem) < 4:
            areaname3 += elem
        #elif len(elem.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')) < 4:
        #        areaname3 += elem.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
        else:
            areaname3 += elem[:4]
    areaname = ''.join(areaname3)
    return areaname + '_' + str(personName[:4]).upper() + '_' + str(problemNumber)


run('individual', 'Documento de avaliação segundo as Heurísticas de Nielsen','Avaliação individual', 'Respostas - HeurNiel', 0, False, False, True, False)
run('consolidado', 'Documento de avaliação segundo as Heurísticas de Nielsen','Avaliação consolidada', 'Respostas - HeurNiel', 1, False, False, True, False)



