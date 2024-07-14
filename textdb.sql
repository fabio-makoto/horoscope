-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: textdb
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `texts`
--
CREATE DATABASE textdb;

USE textdb;



DROP TABLE IF EXISTS `texts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `texts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `horoscope_text` varchar(600) NOT NULL,
  `sign_name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texts`
--

LOCK TABLES `texts` WRITE;
/*!40000 ALTER TABLE `texts` DISABLE KEYS */;
INSERT INTO `texts` VALUES (1,'[b]As características do signo de[/] [bold red]Áries[/]: [i]É Representado pelo elemento fogo e pela cabeça de carneiro como símbolo, o signo de áries é conhecido pelo senso de liderança, autonomia e pioneirismo, assim como pela sua coragem e autoconfiança. Outra característica associada ao primeiro signo do zodíaco é a impulsividade, muitas vezes relacionada a um perfil mais \"explosivo\" e impaciente.','aries'),(2,'As características do signo de [bold red]Touro[/]: [i]Os taurinos têm a terra como elemento e a cabeça de um touro simbolizando o signo, normalmente representada por um círculo com dois chifres. Eles são considerados pessoas leais, protetoras e determinadas. Além disso, o signo é conhecido por gostar de aproveitar os prazeres da vida, como comer e dormir, por exemplo — por isso é associado à preguiça e à gula. Também podem apresentar a teimosia como um aspecto forte de personalidade.\n','taurus'),(3,'[b]As características do signo de[/] [bold red]Gêmeos[/]: [i]O signo de gêmeos é comunicativo, sociável e inteligente. Regido pelo elemento ar e representado pelo número 2 em algarismos romanos, esse é um signo adaptável e tem uma energia ligada ao mental. Geminianos também são conhecidos pela curiosidade e vontade de aprender, o que se relaciona a essa energia mental — que também pode despertar impaciência, ansiedade e superficialidade.','gemini'),(4,'[b]As características do signo de[/] [bold red]Câncer[/]: [i]O significado dos signos se relaciona com o símbolo que os representa e com câncer isso não é diferente. Representado por um caranguejo, esse signo pode ser mais reservado e cauteloso, protegendo suas emoções — assim como o caranguejo se protege em sua casca. Além disso, os cancerianos, regidos pelo elemento água, são conhecidos pela sensibilidade e por serem carinhosos, assim como pela conexão com a família e com o passado. Por outro lado, tem como desafio não alimentar mágoas.','cancer'),(5,'[b]As características do signo de[/] [bold red]Leão[/]: [i]Representados por um leão e regidos pelo elemento fogo, os leoninos apresentam como características a criatividade, o carisma e a generosidade. Esse signo também é associado à coragem, determinação e a autoconfiança — que pode ser relacionada a uma arrogância em alguns momentos. A individualidade também é uma característica que pode atenuar o senso de egocentrismo.','leo'),(6,'[b]As características do signo de[/] [bold red]Virgem[/]: [i]Virgem é um signo de terra, representado pela letra “M” ou pela imagem de uma mulher. Conhecidos pelo senso de organização, os virginianos são determinados, trabalhadores e disciplinados. Ao avaliar o significado dos signos, características como a capacidade analítica e detalhista — muitas vezes relacionadas ao perfeccionismo e ao hipercriticismo — também são relacionados ao signo de virgem, assim como a praticidade e o altruísmo.','virgo'),(7,'[b]As características do signo de[/] [bold red]Libra[/]: [i]Representado pelo símbolo da balança, os librianos são conhecidos pelo senso de justiça e pela diplomacia, assim como pela harmonia e a busca pelo equilíbrio. O signo de libra é regido pelo elemento ar e tem como características associadas a ele a sociabilidade, inteligência e a capacidade de apreciar a beleza das coisas. Tem como desafio aprender a dizer não.','libra'),(8,'[b]As características do signo de[/] [bold red]Escorpião[/]: [i]O signo de escorpião é representado pelo animal de mesmo nome e tem o elemento de água como seu regente. É conhecido pela intensidade e profundidade emocional, assim como pela persistência e o carisma. Além disso, o signo está associado a um interesse por temas esotéricos e mais profundos ou misteriosos. Os escorpianos também têm como características a capacidade de transformação.','scorpio'),(9,'[b]As características do signo de[/] [bold red]Sagitário[/]: [i]O símbolo do Sagitário é uma flecha, associada ao centauro, que também pode aparecer em algumas representações do signo. Ligado ao elemento fogo, é um signo que tem como características o senso de aventura, exploração e sabedoria. Sagitarianos também prezam pela autonomia, a liberdade e pela espontaneidade. Além disso, é um signo relacionado à impulsividade.','sagittarius'),(10,'[b]As características do signo de[/] [bold red]Capricórnio[/]: [i]Regido pelo elemento terra, Capricórnio é representado pela cabra marinha e é um signo conhecido pela determinação, responsabilidade e pelo pragmatismo. Os capricornianos também são trabalhadores, ambiciosos e práticos. Outras características são a busca pela estabilidade, segurança e a capacidade visionária. Vale se atentar em aprender a ser menos solitário.','capricorn'),(11,'[b]As características do signo de[/] [bold red]Aquário[/]: [i]Assim como o significado dos signos de ar, como Gêmeos, aquarianos também tem uma energia mais mental, que confere algumas características relacionadas ao signo, como capacidade analítica, lógica e objetiva. Representado por duas ondas, esse é um signo conhecido pela originalidade, individualidade e sociabilidade. Além disso, Aquário pode ser relacionado a rebeldia, a inovação e a mudanças.','aquarius'),(12,'[b]As características do signo de[/] [bold red]Peixes[/]: [i]Signo de elemento água, Peixes tem como características a sensibilidade, criatividade e a empatia. Representado por dois peixes, o último signo do zodíaco é conhecido por ser sonhador, intuitivo e conectado a emoções. Esse signo também é conhecido pela relação com a arte, capacidade de adaptação e conexão com a espiritualidade.','pisces');
/*!40000 ALTER TABLE `texts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-14 17:53:28
