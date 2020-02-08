-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: jobseek
-- ------------------------------------------------------
-- Server version	8.0.15


 SET NAMES utf8mb4 ;


--
-- Table structure for table `employer`
--

DROP TABLE IF EXISTS `employer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `employer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `companyName` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `logo_url` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyName` (`companyName`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer`
--

LOCK TABLES `employer` WRITE;
/*!40000 ALTER TABLE `employer` DISABLE KEYS */;
INSERT INTO `employer` VALUES (1,'test2','tests@gmail.com','http://job.pharmaglobiz.com/images/default-logo.png'),
                              (2,'matt','matt@mail.com',''),
                              (3,'wwwww','www@dd.com','http://job.pharmaglobiz.com/images/default-logo.png'),
                              (4,'A N Other Builders','admin@ano.com','https://cdn2.vectorstock.com/i/1000x1000/23/96/building-town-construction-logo-vector-19182396.jpg'),
                              (5,'Be Strong','info@strong.com','https://cms-assets.tutsplus.com/uploads/users/151/posts/32516/image/Placeit4.jpg'),
                              (6,'Accounting & Financial Ltd','info@acltd.com','https://realdeals.xyz/wp-content/uploads/2017/09/Accounting-Logo995.jpg'),
                              (7,'Tech Centre','info@tech.com','https://nice-assets-3.s3-accelerate.amazonaws.com/smart_templates/39b376b36ad04b7b89b6db4e75871711/assets/preview_fdc588c8e359e677cd4a517865bfd584.jpg'),
                              (8,'Digi tech','admin@digi.com','https://cdn1.vectorstock.com/i/1000x1000/26/20/icon-hi-tech-company-logo-design-business-vector-20812620.jpg'),
                              (9,'Base Over Apex','info@base.com','https://i.pinimg.com/originals/7c/33/f3/7c33f3eb1e875e327d49eaa4e0670c33.jpg'),
                              (10,'test','test@admin.com','http://job.pharmaglobiz.com/images/default-logo.png');
/*!40000 ALTER TABLE `employer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_post`
--

DROP TABLE IF EXISTS `job_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `job_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_posted` datetime NOT NULL,
  `title` varchar(60) NOT NULL,
  `jobType` varchar(40) NOT NULL,
  `salary` varchar(15) NOT NULL,
  `role_sum` text NOT NULL,
  `resp` text NOT NULL,
  `requirements` text NOT NULL,
  `how_to_apply` text NOT NULL,
  `emp_id` int(11) NOT NULL,
  `sector_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emp_id` (`emp_id`),
  KEY `sector_id` (`sector_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `job_post_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employer` (`id`),
  CONSTRAINT `job_post_ibfk_2` FOREIGN KEY (`sector_id`) REFERENCES `sector` (`id`),
  CONSTRAINT `job_post_ibfk_3` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_post`
--

LOCK TABLES `job_post` WRITE;
/*!40000 ALTER TABLE `job_post` DISABLE KEYS */;
INSERT INTO `job_post` VALUES (5,'2019-05-08 22:41:17','Various apprenticeships in construction','Full-time','10000+','<p>You&rsquo;ll learn on the job, and in a locally approved college &ndash; and you&rsquo;ll be earning all the time. At the end of the two years, you&rsquo;ll have loads more experience and valuable job skills, plus a technical certificate and nationally recognised apprenticeship qualification.</p>\r\n','<p>You need to be aged between 16 and 23 years old and prepared to commit yourself to at least two years of training and study. We&rsquo;re looking for individuals who are ambitious, enthusiastic and willing to learn. The nature of the work can be very involved, so you need to be prepared to work outdoors.&nbsp;You need to be focussed on the career you want. You&rsquo;ll need to demonstrate that you have fully researched the area of work you want to do, and that you&rsquo;re the right person for the job. You&rsquo;ll also need to be prepared to work hard to get your qualification by learning on the job, and undertaking further studies.</p>\r\n','<p>You need to be aged between 16 and 23 years old and prepared to commit yourself to at least two years of training and study. We&rsquo;re looking for individuals who are ambitious, enthusiastic and willing to learn. The nature of the work can be very involved, so you need to be prepared to work outdoors.&nbsp;You need to be focussed on the career you want. You&rsquo;ll need to demonstrate that you have fully researched the area of work you want to do, and that you&rsquo;re the right person for the job. You&rsquo;ll also need to be prepared to work hard to get your qualification by learning on the job, and undertaking further studies.</p>\r\n','<p>Email <strong>admin@ano.com</strong> with interest</p>\r\n',4,6,84),
                              (6,'2019-05-08 22:45:31','Gym Assistant','Full-time','20000+','<p>The Fitness Assistant assists the Fitness Staff in monitoring the floor, keeping the equipment clean and well maintained. This position has excellent communication skills and is conscious of the needs of the members to assist in their workout</p>\r\n','<ul>\r\n	<li>Setting up/clearing away after group sessions</li>\r\n	<li>Cleaning and maintaining equipment, ensuring it is always safe to use</li>\r\n	<li>Cleaning gym areas, corridors and changing rooms</li>\r\n	<li>Working on reception &ndash; checking membership cards, taking payments, booking sessions, processing new members/membership renewals</li>\r\n	<li>Answering the telephone and resolving customer enquiries</li>\r\n</ul>\r\n','<ul>\r\n	<li>Customer service experience not essential but would be an advantage</li>\r\n	<li>Experience using the full range of gym equipment</li>\r\n	<li>Basic understanding of health and safety in gym environments</li>\r\n	<li>Basic IT skills</li>\r\n</ul>\r\n','<p>Call Ben on 072929294848</p>\r\n',5,22,95),
                              (7,'2019-05-08 22:56:03','Accounts Administration','Full-time','20000+','<p>We are looking for an Accounts Administrator to manage our company&rsquo;s accounts payable and receivable.</p>\r\n','<ul>\r\n	<li>Manage obligations to suppliers, customers and third-party vendors</li>\r\n	<li>Process bank deposits</li>\r\n	<li>Reconcile financial statements</li>\r\n	<li>Prepare, send and store invoices</li>\r\n	<li>Contact clients and send reminders to ensure timely payments</li>\r\n	<li>Submit tax forms</li>\r\n	<li>Identify and address discrepancies</li>\r\n	<li>Report on the status of accounts payable and receivable</li>\r\n	<li>Update internal accounting databases and spreadsheets</li>\r\n</ul>\r\n','<ul>\r\n	<li>Proven work experience as an Accounts Administrator or similar role</li>\r\n	<li>Good knowledge of bookkeeping procedures and debt collection regulations</li>\r\n	<li>Hands-on experience with accounting software</li>\r\n	<li>Advanced knowledge of Excel (using financial formulas and creating spreadsheets)</li>\r\n	<li>Solid data entry skills with an ability to identify numerical errors</li>\r\n	<li>Good organizational and time-management abilities</li>\r\n	<li>BSc degree in Finance, Accounting or relevant field</li>\r\n</ul>\r\n','<p>Email&nbsp;<strong>info@afltd.com</strong>&nbsp;with your CV</p>\r\n',6,3,4),
                              (8,'2019-05-08 23:04:45','Senior Python Developer','Full-time','50000+','<p>We are looking for a Senior Python Developer to build functional and efficient server-side applications. If you&rsquo;re a seasoned developer with a love for back-end technologies, we&rsquo;d like to meet you. Your ultimate goal is to create high-quality products that meet customer needs.</p>\r\n','<ul>\r\n	<li>Help design and implement functional requirements</li>\r\n	<li>Build efficient back-end features in Python</li>\r\n	<li>Integrate front-end components into applications</li>\r\n	<li>Manage testing and bug fixes</li>\r\n	<li>Prepare technical documentation</li>\r\n	<li>Collaborate with UX/UI designers to implement design into the code</li>\r\n	<li>Coach junior team members</li>\r\n	<li>Implement software enhancements and suggest improvements</li>\r\n</ul>\r\n','<ul>\r\n	<li>Solid experience as Python Developer</li>\r\n	<li>Experience with Python frameworks (e.g. Django, Flask, Bottle)</li>\r\n	<li>Familiarity with Amazon Web Services (AWS) and REST API</li>\r\n	<li>Understanding of databases and SQL</li>\r\n	<li>Knowledge of JavaScript and the AngularJS framework is a plus</li>\r\n	<li>Attention to detail</li>\r\n	<li>Leadership skills</li>\r\n	<li>BSc in Computer Science, Engineering or relevant field</li>\r\n</ul>\r\n','<p>Call <strong>Jen&nbsp;</strong>on 07282838492 for an informal introduction</p>\r\n',7,1,110),
                              (9,'2019-05-08 23:07:37','iOS Developer','Full-time','40000+','<p>We are looking for an iOS developer who possesses a passion for pushing mobile technologies to the limits and will work with our team of talented engineers to design and build the next generation of our mobile applications.</p>\r\n','<ul>\r\n	<li>Design and build advanced applications for the iOS platform</li>\r\n	<li>Collaborate with cross-functional teams to define, design, and ship new features.</li>\r\n	<li>Unit-test code for robustness, including edge cases, usability, and general reliability.</li>\r\n	<li>Work on bug fixing and improving application performance.</li>\r\n	<li>Continuously discover, evaluate, and implement new technologies to maximize development efficiency.</li>\r\n</ul>\r\n','<ul>\r\n	<li>BS/MS degree in Computer Science, Engineering or a related subject</li>\r\n	<li>Proven working experience in software development</li>\r\n	<li>Working experience in iOS development</li>\r\n	<li>Have published one or more iOS apps in the app store</li>\r\n	<li>A deep familiarity with Objective-C and Cocoa Touch</li>\r\n	<li>Experience working with iOS frameworks such as Core Data, Core Animation, Core Graphics and Core Text</li>\r\n	<li>Experience with third-party libraries and APIs</li>\r\n	<li>Working knowledge of the general mobile landscape, architectures, trends, and emerging technologies</li>\r\n	<li>Solid understanding of the full mobile development life cycle</li>\r\n</ul>\r\n','<p>Email us at <strong>admin@digi</strong>.com with your CV</p>\r\n',8,1,202),
                              (10,'2019-05-08 23:11:25','Sales Trainer','Part-time','30000+','<p>We are looking for a Sales Trainer to design and deliver educational programs for our sales teams.&nbsp;Ultimately, you will help increase the overall performance of our sales teams and ensure they have the skills to achieve their goals.</p>\r\n','<ul>\r\n	<li>Conduct skills gap analyses to identify areas of improvement</li>\r\n	<li>Design training curricula within time and budget constraints</li>\r\n	<li>Produce physical and digital educational material (e.g. videos and case studies)</li>\r\n	<li>Onboard new salespeople</li>\r\n	<li>Coordinate individual and team performance review sessions to discuss strengths and weaknesses</li>\r\n	<li>Monitor sales objectives and results</li>\r\n	<li>Collect feedback from trainees and managers about training courses</li>\r\n	<li>Report on impact of training programs (e.g. sales achieved)</li>\r\n	<li>Liaise with external trainers or industry professionals and organize seminars</li>\r\n	<li>Maintain updated records of training material, curricula and costs</li>\r\n</ul>\r\n','<ul>\r\n	<li>Proven work experience as a Sales Trainer or similar role</li>\r\n	<li>Experience in a sales position is a plus</li>\r\n	<li>Ability to manage the full training cycle, including in-person activities and web-based learning</li>\r\n	<li>Hands-on experience with e-learning platforms</li>\r\n	<li>Excellent organizational skills</li>\r\n	<li>Solid communication and presentation abilities</li>\r\n	<li>BSc degree in Education, Human Resources or relevant field</li>\r\n	<li>Additional certification in training is a plus</li>\r\n</ul>\r\n','<p>Email Ben at <strong>info@base.com</strong></p>\r\n',9,20,68);
/*!40000 ALTER TABLE `job_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(30) NOT NULL,
  `country` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Aberdeen','SCO'),(2,'Aldershot','ENG'),(3,'Altrincham','ENG'),(4,'Ashford','ENG'),(5,'Atherton','ENG'),(6,'Aylesbury','ENG'),(7,'Bamber Bridge','ENG'),(8,'Bangor','NIR'),(9,'Barnsley','ENG'),(10,'Barry','WAL'),(11,'Basildon','ENG'),(12,'Basingstoke','ENG'),(13,'Bath','ENG'),(14,'Batley','ENG'),(15,'Bebington','ENG'),(16,'Bedford','ENG'),(17,'Beeston','ENG'),(18,'Belfast','NIR'),(19,'Birkenhead','ENG'),(20,'Birmingham','ENG'),(21,'Blackburn','ENG'),(22,'Blackpool','ENG'),(23,'Bloxwich','ENG'),(24,'Bognor Regis','ENG'),(25,'Bolton','ENG'),(26,'Bootle','ENG'),(27,'Bournemouth','ENG'),(28,'Bracknell','ENG'),(29,'Bradford','ENG'),(30,'Brentwood','ENG'),(31,'Brighton and Hove','ENG'),(32,'Bristol','ENG'),(33,'Burnley','ENG'),(34,'Burton upon Trent','ENG'),(35,'Bury','ENG'),(36,'Cambridge (/ Milton)','ENG'),(37,'Cannock','ENG'),(38,'Canterbury','ENG'),(39,'Cardiff','WAL'),(40,'Carlisle','ENG'),(41,'Carlton','ENG'),(42,'Chatham','ENG'),(43,'Chelmsford','ENG'),(44,'Cheltenham','ENG'),(45,'Chester','ENG'),(46,'Chesterfield','ENG'),(47,'Christchurch','ENG'),(48,'Clacton-on-Sea','ENG'),(49,'Colchester','ENG'),(50,'Corby','ENG'),(51,'Coventry','ENG'),(52,'Crawley','ENG'),(53,'Crewe','ENG'),(54,'Crosby','ENG'),(55,'Cumbernauld','SCO'),(56,'Darlington','ENG'),(57,'Derby','ENG'),(58,'Derry (Londonderry)','NIR'),(59,'Dewsbury','ENG'),(60,'Doncaster','ENG'),(61,'Dudley','ENG'),(62,'Dundee','SCO'),(63,'Dunfermline','SCO'),(64,'Durham','ENG'),(65,'Eastbourne','ENG'),(66,'East Kilbride','SCO'),(67,'Eastleigh','ENG'),(68,'Edinburgh','SCO'),(69,'Ellesmere Port','ENG'),(70,'Esher','ENG'),(71,'Ewell','ENG'),(72,'Exeter','ENG'),(73,'Farnborough','ENG'),(74,'Filton','ENG'),(75,'Folkestone','ENG'),(76,'Gateshead','ENG'),(77,'Gillingham','ENG'),(78,'Glasgow','SCO'),(79,'Gloucester','ENG'),(80,'Gosport','ENG'),(81,'Gravesend','ENG'),(82,'Grays','ENG'),(83,'Grimsby','ENG'),(84,'Guildford','ENG'),(85,'Halesowen','ENG'),(86,'Halifax','ENG'),(87,'Hamilton','SCO'),(88,'Harlow','ENG'),(89,'Harrogate','ENG'),(90,'Hartlepool','ENG'),(91,'Hastings','ENG'),(92,'Hemel Hempstead','ENG'),(93,'Hereford','ENG'),(94,'High Wycombe','ENG'),(95,'Huddersfield','ENG'),(96,'Ipswich','ENG'),(97,'Keighley','ENG'),(98,'Kettering','ENG'),(99,'Kidderminster','ENG'),(100,'Kingston upon Hull (Hull)','ENG'),(101,'Kingswinford','ENG'),(102,'Kirkcaldy','SCO'),(103,'Lancaster','ENG'),(104,'Leeds','ENG'),(105,'Leicester','ENG'),(106,'Lincoln','ENG'),(107,'Littlehampton','ENG'),(108,'Liverpool','ENG'),(109,'Livingston','SCO'),(110,'London','ENG'),(111,'Loughborough','ENG'),(112,'Lowestoft','ENG'),(113,'Luton','ENG'),(114,'Macclesfield','ENG'),(115,'Maidenhead','ENG'),(116,'Maidstone','ENG'),(117,'Manchester','ENG'),(118,'Mansfield','ENG'),(119,'Margate','ENG'),(120,'Middlesbrough','ENG'),(121,'Milton Keynes','ENG'),(122,'Neath','WAL'),(123,'Newcastle-under-Lyme','ENG'),(124,'Newcastle upon Tyne','ENG'),(125,'Newport','WAL'),(126,'Newtownabbey','NIR'),(127,'Northampton','ENG'),(128,'Norwich','ENG'),(129,'Nottingham','ENG'),(130,'Nuneaton','ENG'),(131,'Oldham','ENG'),(132,'Oxford','ENG'),(133,'Paignton','ENG'),(134,'Paisley','SCO'),(135,'Peterborough','ENG'),(136,'Plymouth','ENG'),(137,'Poole','ENG'),(138,'Portsmouth','ENG'),(139,'Preston','ENG'),(140,'Rayleigh','ENG'),(141,'Reading','ENG'),(142,'Redditch','ENG'),(143,'Rochdale','ENG'),(144,'Rochester','ENG'),(145,'Rotherham','ENG'),(146,'Royal Leamington Spa','ENG'),(147,'Royal Tunbridge Wells','ENG'),(148,'Rugby','ENG'),(149,'Runcorn','ENG'),(150,'Sale','ENG'),(151,'Salford','ENG'),(152,'Scarborough','ENG'),(153,'Scunthorpe','ENG'),(154,'Sheffield','ENG'),(155,'Shoreham-by-Sea','ENG'),(156,'Shrewsbury','ENG'),(157,'Sittingbourne','ENG'),(158,'Slough','ENG'),(159,'Smethwick','ENG'),(160,'Solihull','ENG'),(161,'Southampton','ENG'),(162,'Southend-on-Sea','ENG'),(163,'Southport','ENG'),(164,'South Shields','ENG'),(165,'Stafford','ENG'),(166,'St Albans','ENG'),(167,'Stevenage','ENG'),(168,'St Helens','ENG'),(169,'Stockport','ENG'),(170,'Stockton-on-Tees','ENG'),(171,'Stoke-on-Trent','ENG'),(172,'Stourbridge','ENG'),(173,'Sunderland','ENG'),(174,'Sutton Coldfield','ENG'),(175,'Swansea','WAL'),(176,'Swindon','ENG'),(177,'Tamworth','ENG'),(178,'Taunton','ENG'),(179,'Telford','ENG'),(180,'Torquay','ENG'),(181,'Tynemouth','ENG'),(182,'Wakefield','ENG'),(183,'Wallasey','ENG'),(184,'Walsall','ENG'),(185,'Walton-on-Thames','ENG'),(186,'Warrington','ENG'),(187,'Washington','ENG'),(188,'Watford','ENG'),(189,'Wellingborough','ENG'),(190,'Welwyn Garden City','ENG'),(191,'West Bromwich','ENG'),(192,'Weston-super-Mare','ENG'),(193,'Weymouth','ENG'),(194,'Widnes','ENG'),(195,'Wigan','ENG'),(196,'Willenhall','ENG'),(197,'Woking','ENG'),(198,'Wolverhampton','ENG'),(199,'Worcester','ENG'),(200,'Worthing','ENG'),(201,'Wrexham','WAL'),(202,'York','ENG');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sector`
--

DROP TABLE IF EXISTS `sector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sector` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sector`
--

LOCK TABLES `sector` WRITE;
/*!40000 ALTER TABLE `sector` DISABLE KEYS */;
INSERT INTO `sector` VALUES (1,'IT'),(2,'Admin'),(3,'Accountancy/Finance'),(4,'Charity'),(5,'Business Management/Consulting'),(6,'Construction/Property'),(7,'Energy/Utilities'),(8,'Engineering/Manufacturing'),(9,'Environment/Agriculture'),(10,'Healthcare'),(11,'Hospitality'),(12,'HR & Recruitment'),(13,'IT (Information Technology)'),(14,'Law'),(15,'Leisure/Tourism'),(16,'Logistics/Transport'),(17,'Marketing/Digital Media'),(18,'Public Sector/Services'),(19,'Retail'),(20,'Sales'),(21,'Teaching/Education'),(22,'Fitness/Leisure'),(23,'Hair Dressing'),(24,'Cosmetics');
/*!40000 ALTER TABLE `sector` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-22 17:49:23
