from flask_restful import Resource, reqparse

vars = [
 {'nm_var': 'NU_ANO_CENSO', 'ds_var': 'Ano de referencia do Censo Superior'},
 {'nm_var': 'CO_IES', 'ds_var': 'Codigo unico de identificacao da IES'},
 {'nm_var': 'TP_CATEGORIA_ADMINISTRATIVA',
  'ds_var': 'Tipo da Categoria Administrativa da IES'},
 {'nm_var': 'TP_ORGANIZACAO_ACADEMICA',
  'ds_var': 'Tipo da Organizacao Academica da IES'},
 {'nm_var': 'CO_CURSO',
  'ds_var': 'Codigo unico de identificacao do curso gerado pelo E-MEC'},
 {'nm_var': 'CO_CURSO_POLO',
  'ds_var': 'Codigo de identificacao do polo vinculado ao curso'},
 {'nm_var': 'TP_TURNO',
  'ds_var': 'Tipo do turno do curso ao qual o aluno esta vinculado'},
 {'nm_var': 'TP_GRAU_ACADEMICO',
  'ds_var': 'Tipo do grau academico conferido ao diplomado pelo curso'},
 {'nm_var': 'TP_MODALIDADE_ENSINO',
  'ds_var': 'Tipo da modalidade de ensino do curso'},
 {'nm_var': 'TP_NIVEL_ACADEMICO',
  'ds_var': 'Tipo do nivel academico do curso'},
 {'nm_var': 'CO_CINE_ROTULO',
  'ds_var': 'Codigo de identificacao do curso, a partir de uma adaptacao da metodologia internacional de classificacao Eurostat/ Unesco/ OCDE'},
 {'nm_var': 'ID_ALUNO',
  'ds_var': 'Codigo de identificacao gerado pelo Inep para o aluno da educacao superior'},
 {'nm_var': 'CO_ALUNO_CURSO',
  'ds_var': 'Codigo de identificacao gerado pelo Inep para o vinculo do aluno ao curso'},
 {'nm_var': 'CO_ALUNO_CURSO_ORIGEM',
  'ds_var': 'Codigo de identificacao gerado pelo Inep para o vinculo do aluno em seu curso de origem, ou seja, de onde foi transferido.'},
 {'nm_var': 'TP_COR_RACA', 'ds_var': 'Tipo da cor/raca do aluno'},
 {'nm_var': 'TP_SEXO', 'ds_var': 'Informa o sexo do aluno'},
 {'nm_var': 'NU_ANO_NASCIMENTO', 'ds_var': 'Ano de nascimento do aluno'},
 {'nm_var': 'NU_MES_NASCIMENTO', 'ds_var': 'Mes de nascimento do aluno'},
 {'nm_var': 'NU_DIA_NASCIMENTO', 'ds_var': 'Dia de nascimento do aluno'},
 {'nm_var': 'NU_IDADE',
  'ds_var': 'Idade que o aluno completa no ano de referencia do Censo'},
 {'nm_var': 'TP_NACIONALIDADE', 'ds_var': 'Tipo da nacionalidade do aluno'},
 {'nm_var': 'CO_PAIS_ORIGEM',
  'ds_var': 'Codigo do pais de nascimento ou de naturalizacao do aluno estrangeiro'},
 {'nm_var': 'CO_UF_NASCIMENTO',
  'ds_var': 'Codigo do IBGE da Unidade da Federacao de nascimento do aluno'},
 {'nm_var': 'CO_MUNICIPIO_NASCIMENTO',
  'ds_var': 'Codigo do IBGE do municipio de nascimento do aluno'},
 {'nm_var': 'IN_DEFICIENCIA',
  'ds_var': 'Informa se o aluno e uma pessoa com deficiencia, transtorno global do desenvolvimento ou altas habilidades/superdotacao'},
 {'nm_var': 'IN_DEFICIENCIA_AUDITIVA',
  'ds_var': 'Informa se o aluno e uma pessoa com deficiencia auditiva'},
 {'nm_var': 'IN_DEFICIENCIA_FISICA',
  'ds_var': 'Informa se o aluno e uma pessoa com deficiencia fisica'},
 {'nm_var': 'IN_DEFICIENCIA_INTELECTUAL',
  'ds_var': 'Informa se o aluno e uma pessoa com deficiencia intelectual'},
 {'nm_var': 'IN_DEFICIENCIA_MULTIPLA',
  'ds_var': 'Informa se o aluno e uma pessoa com deficiencia multipla'},
 {'nm_var': 'IN_DEFICIENCIA_SURDEZ',
  'ds_var': 'Informa se o aluno e uma pessoa surda'},
 {'nm_var': 'IN_DEFICIENCIA_SURDOCEGUEIRA',
  'ds_var': 'Informa se o aluno e uma pessoa com surdocegueira'},
 {'nm_var': 'IN_DEFICIENCIA_BAIXA_VISAO',
  'ds_var': 'Informa se o aluno e uma pessoa com baixa visao'},
 {'nm_var': 'IN_DEFICIENCIA_CEGUEIRA',
  'ds_var': 'Informa se o aluno e uma pessoa cega '},
 {'nm_var': 'IN_DEFICIENCIA_SUPERDOTACAO',
  'ds_var': 'Informa se o aluno e uma pessoa com altas habilidades/superdotacao'},
 {'nm_var': 'IN_TGD_AUTISMO',
  'ds_var': 'Informa se o aluno e uma pessoa com autismo infantil'},
 {'nm_var': 'IN_TGD_SINDROME_ASPERGER',
  'ds_var': 'Informa se o aluno e uma pessoa com Sindrome de Asperger'},
 {'nm_var': 'IN_TGD_SINDROME_RETT',
  'ds_var': 'Informa se o aluno e uma pessoa com Sindrome de Rett'},
 {'nm_var': 'IN_TGD_TRANSTOR_DESINTEGRATIVO',
  'ds_var': 'Informa se o aluno e uma pessoa com Transtorno Desintegrativo da Infancia'},
 {'nm_var': 'TP_SITUACAO',
  'ds_var': 'Tipo de situacao de vinculo do aluno no curso'},
 {'nm_var': 'QT_CARGA_HORARIA_TOTAL',
  'ds_var': 'Somatorio do total da carga horaria dos componentes curriculares que fazem parte da matriz do curso'},
 {'nm_var': 'QT_CARGA_HORARIA_INTEG',
  'ds_var': 'Somatorio da carga horaria dos componentes curriculares que o aluno tenha aproveitado e que fazem parte da matriz do curso'},
 {'nm_var': 'DT_INGRESSO_CURSO',
  'ds_var': 'Data de ingresso do aluno no curso correspondente ao 1o semestre (01/01/2015) e ao 2o semestre (01/07/2015)'},
 {'nm_var': 'IN_INGRESSO_VESTIBULAR',
  'ds_var': 'Informa se o aluno ingressou no curso por vestibular. '},
 {'nm_var': 'IN_INGRESSO_ENEM',
  'ds_var': 'Informa se o aluno ingressou no curso pelo Enem. '},
 {'nm_var': 'IN_INGRESSO_AVALIACAO_SERIADA',
  'ds_var': 'Informa se o aluno ingressou no curso por meio da Avaliacao Seriada'},
 {'nm_var': 'IN_INGRESSO_SELECAO_SIMPLIFICA',
  'ds_var': 'Informa se o aluno ingressou no curso por meio de selecao simplificada'},
 {'nm_var': 'IN_INGRESSO_OUTRO_TIPO_SELECAO',
  'ds_var': 'Informa se o aluno ingressou no curso por outros tipos de selecao.'},
 {'nm_var': 'IN_INGRESSO_VAGA_REMANESC',
  'ds_var': 'Informa se o aluno ingressou no curso por  meio de vagas remanescentes'},
 {'nm_var': 'IN_INGRESSO_VAGA_PROG_ESPECIAL',
  'ds_var': 'Informa se  o aluno ingressou no curso por meio de vagas para programas especiais'},
 {'nm_var': 'IN_INGRESSO_TRANSF_EXOFFICIO',
  'ds_var': 'Informa se o aluno ingressou no curso  por meio de Transferencia Ex-officio'},
 {'nm_var': 'IN_INGRESSO_DECISAO_JUDICIAL',
  'ds_var': 'Informa se o aluno ingressou no curso por meio de decisao judicial'},
 {'nm_var': 'IN_INGRESSO_CONVENIO_PECG',
  'ds_var': 'Informa se o aluno ingressou no curso por programa de convenio para estudantes estrangeiros '},
 {'nm_var': 'IN_INGRESSO_EGRESSO',
  'ds_var': 'Forma de ingresso que indica que o aluno se formou em um curso de Bacharelado Interdisciplinar ou Licenciatura Interdisciplinar e que ingressou em um curso de terminalidade.'},
 {'nm_var': 'IN_INGRESSO_OUTRA_FORMA',
  'ds_var': 'Informa se o aluno ingressou no curso por outras formas de ingresso.'},
 {'nm_var': 'IN_RESERVA_VAGAS',
  'ds_var': 'Informa se o aluno participa de programa de reserva de vagas" '},
 {'nm_var': 'IN_RESERVA_ETNICO',
  'ds_var': 'Informa se o aluno ingressou por meio de programa de reserva de vagas de cunho etnico'},
 {'nm_var': 'IN_RESERVA_DEFICIENCIA',
  'ds_var': 'informa se o aluno ingressou por meio de programa de reserva de vagas para pessoas com deficiencia'},
 {'nm_var': 'IN_RESERVA_ENSINO_PUBLICO',
  'ds_var': ' Informa se o aluno ingressou por meio de programa de reserva de vagas para egressos da escola publica'},
 {'nm_var': 'IN_RESERVA_RENDA_FAMILIAR',
  'ds_var': 'Informa se o aluno ingressou por meio de programa de reserva de vagas de cunho social/renda familiar'},
 {'nm_var': 'IN_RESERVA_OUTRA',
  'ds_var': 'Informa se o aluno ingressou por meio de programas de reserva de vagas diferentes dos seguintes tipos : etnico, pessoa com deficiencia, estudante procedente de escola publica, social/renda familiar '},
 {'nm_var': 'IN_FINANCIAMENTO_ESTUDANTIL',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil'},
 {'nm_var': 'IN_FIN_REEMB_FIES',
  'ds_var': 'Informa se o aluno utiliza o Fundo de Financiamento Estudantil (Fies) como forma de financimanto estudantil reembolsavel'},
 {'nm_var': 'IN_FIN_REEMB_ESTADUAL',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil reembolsavel do governo estadual'},
 {'nm_var': 'IN_FIN_REEMB_MUNICIPAL',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil reembolsavel do governo municipal'},
 {'nm_var': 'IN_FIN_REEMB_PROG_IES',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil reembolsavel administrado pela IES'},
 {'nm_var': 'IN_FIN_REEMB_ENT_EXTERNA',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil reembolsavel administrado por entidades externas a IES'},
 {'nm_var': 'IN_FIN_REEMB_OUTRA',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil reembolsavel administrado por outras entidades'},
 {'nm_var': 'IN_FIN_NAOREEMB_PROUNI_INTEGR',
  'ds_var': 'Informa se o aluno e bolsista integral do Programa Universidade para Todos (Prouni), tipo de financiamento estudantil nao reembolsavel'},
 {'nm_var': 'IN_FIN_NAOREEMB_PROUNI_PARCIAL',
  'ds_var': 'Informa se o aluno e bolsista parcial do Programa Universidade para Todos (Prouni), tipo de financiamento estudantil nao reembolsavel'},
 {'nm_var': 'IN_FIN_NAOREEMB_ESTADUAL',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil estadual nao reembolsavel'},
 {'nm_var': 'IN_FIN_NAOREEMB_MUNICIPAL',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil municipal nao reembolsavel'},
 {'nm_var': 'IN_FIN_NAOREEMB_PROG_IES',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil nao reembolsavel administrado pela IES'},
 {'nm_var': 'IN_FIN_NAOREEMB_ENT_EXTERNA',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil nao reembolsavel administrado por entidades externas a IES'},
 {'nm_var': 'IN_FIN_NAOREEMB_OUTRA',
  'ds_var': 'Informa se o aluno utiliza financiamento estudantil nao reembolsavel administrado por outras formas'},
 {'nm_var': 'IN_APOIO_SOCIAL',
  'ds_var': 'Informa se o aluno recebe algum tipo de apoio social na forma de moradia, transporte, alimentacao, material didatico e bolsas (trabalho/permanencia)'},
 {'nm_var': 'IN_APOIO_ALIMENTACAO',
  'ds_var': 'Informa se o aluno recebe apoio alimentacao'},
 {'nm_var': 'IN_APOIO_BOLSA_PERMANENCIA',
  'ds_var': 'Informa se o aluno recebe auxilio financeiro destinado a alunos em situacao de vulnerabilidade socioeconomica ou pertencente a grupos etnicos especificos'},
 {'nm_var': 'IN_APOIO_BOLSA_TRABALHO',
  'ds_var': 'Informa se o aluno recebe remuneracao referente a trabalhos prestados nas dependencias da IES ou unidades vinculadas'},
 {'nm_var': 'IN_APOIO_MATERIAL_DIDATICO',
  'ds_var': 'Informa se o aluno recebe apoio para aquisicao de material didatico'},
 {'nm_var': 'IN_APOIO_MORADIA',
  'ds_var': 'Informa se o aluno recebe apoio moradia. '},
 {'nm_var': 'IN_APOIO_TRANSPORTE',
  'ds_var': 'Informa se o aluno recebe apoio para transporte ate a IES'},
 {'nm_var': 'IN_ATIVIDADE_EXTRACURRICULAR',
  'ds_var': 'Informa se o aluno participa de algum tipo de atividade extracurricular (estagio nao obrigatorio, extensao, monitoria e pesquisa)'},
 {'nm_var': 'IN_COMPLEMENTAR_ESTAGIO',
  'ds_var': 'Informa se o aluno faz atividade extracurricular de estagio nao obrigatorio visando ao seu aperfeicoamento profissional'},
 {'nm_var': 'IN_COMPLEMENTAR_EXTENSAO',
  'ds_var': 'Informa se o aluno participa de atividade extracurricular de extensao'},
 {'nm_var': 'IN_COMPLEMENTAR_MONITORIA',
  'ds_var': 'Informa se o aluno participa de atividade extracurricular de monitoria'},
 {'nm_var': 'IN_COMPLEMENTAR_PESQUISA',
  'ds_var': 'Informa se o aluno participa de atividade extracurricular de pesquisa'},
 {'nm_var': 'IN_BOLSA_ESTAGIO',
  'ds_var': 'Informa se o aluno recebe bolsa/remuneracao por fazer atividade extracurricular de estagio nao obrigatorio. '},
 {'nm_var': 'IN_BOLSA_EXTENSAO',
  'ds_var': 'Informa se o aluno recebe bolsa/remuneracaopor participar de atividade extracurricular de extensao. '},
 {'nm_var': 'IN_BOLSA_MONITORIA',
  'ds_var': 'Informa se o aluno recebe bolsa/remuneracao por participar de atividade extracurricular de monitoria. '},
 {'nm_var': 'IN_BOLSA_PESQUISA',
  'ds_var': 'Informa se o aluno recebe bolsa/remuneracao por participar de atividade extracurricular de pesquisa.'},
 {'nm_var': 'TP_ESCOLA_CONCLUSAO_ENS_MEDIO',
  'ds_var': 'Tipo de escola que o aluno concluiu ensino medio'},
 {'nm_var': 'IN_ALUNO_PARFOR',
  'ds_var': 'Informa se o aluno participa do programa especial para a formacao de professores em exercicio na rede publica de educacao basica (PARFOR)'},
 {'nm_var': 'TP_SEMESTRE_CONCLUSAO',
  'ds_var': 'Semestre (do ano de referencia do Censo) em que o aluno se formou'},
 {'nm_var': 'TP_SEMESTRE_REFERENCIA',
  'ds_var': 'Semestre de referencia do preenchimento do vinculo do curso'},
 {'nm_var': 'IN_MOBILIDADE_ACADEMICA',
  'ds_var': 'Informa se o aluno esta regularmente matriculado em curso de graduacao, que se vincula temporariamente a outra instituicao, sendo ela nacional ou internacional'},
 {'nm_var': 'TP_MOBILIDADE_ACADEMICA',
  'ds_var': 'Tipo de mobilidade academica ao qual o aluno participa.'},
 {'nm_var': 'TP_MOBILIDADE_ACADEMICA_INTERN',
  'ds_var': 'Tipo de mobilidade academica internacional ao qual o aluno participa.'},
 {'nm_var': 'CO_IES_DESTINO',
  'ds_var': 'Codigo da instituicao nacional receptora do aluno em mobilidade academica, na qual seu vinculo e temporario'},
 {'nm_var': 'CO_PAIS_DESTINO',
  'ds_var': 'Codigo do pais da instituicao receptora do aluno em mobilidade academica, na qual seu vinculo e temporario'},
 {'nm_var': 'IN_MATRICULA',
  'ds_var': 'Informa se o aluno e matriculado no curso'},
 {'nm_var': 'IN_CONCLUINTE', 'ds_var': 'Informa se o aluno e concluinte'},
 {'nm_var': 'IN_INGRESSO_TOTAL',
  'ds_var': 'Informa se o aluno e ingressante no curso, nao importando a forma de ingresso utilizada.'},
 {'nm_var': 'IN_INGRESSO_VAGA_NOVA',
  'ds_var': 'Informa se o aluno e ingressante no curso por meio de processo seletivo de vaga nova.'},
 {'nm_var': 'IN_INGRESSO_PROCESSO_SELETIVO',
  'ds_var': 'Informa se o aluno ingressou no curso por meio de processo seletivo principal'},
 {'nm_var': 'NU_ANO_INGRESSO', 'ds_var': 'Ano de ingresso do aluno no curso'}
 ]

class Campos(Resource):
    def get(self):
        return {'campos': vars}

class Campo(Resource):
    def get(self, nm_var):    
        temp = nm_var.split(',')
        print(temp)
        for campo in vars:
            if campo['nm_var'] == nm_var:
                print(campo)
                return campo
            else:
                for i in temp:
                    if campo['nm_var'] == i:
                        print(campo)
                        return campo 
        return {'message':'campo não encontrado'}, 404

    def post(self, nm_var):
        par = reqparse.RequestParser()
        par.add_argument('nome')

        data = par.parse_args()

