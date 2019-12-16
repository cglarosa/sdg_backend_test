from main import db,Sdg_goals,User
db.create_all()

user = User(password="password",username="test1",educ_attain="Masters",name="Juan",yrs_exp="Less than 5 years",primary_aff="Office of the President",
	secondary_aff="UP Diliman",acknowledge=True,pending=False,contact_person="Dr. Bongolan")
db.session.add(user)
user = User(password="password",username="test2",educ_attain="Masters",name="Two",yrs_exp="Less than 5 years",primary_aff="Office of the President",
	secondary_aff="UP Diliman",acknowledge=False,pending=True,contact_person="Dr. Bongolan")
db.session.add(user)


goal = Sdg_goals(goal_id="1",subgoal_id="title",body="No poverty")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="0",body="End poverty in all its forms everywhere")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="1",body="By 2030, eradicate extreme poverty for all people everywhere,"
	+ " currently measured as people living on less than $1.25 a day")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="2",body="By 2030, reduce at least by half the proportion of men, women and"
	+ " children of all ages living in poverty in all its dimensions according to national definitions")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="3",body="Implement nationally appropriate social protection systems and measures"
	+ " for all, including floors, and by 2030 achieve substantial coverage of the poor and the vulnerable")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="4",body="By 2030, ensure that all men and women, in particular the poor and the vulnerable,"
	+ " have equal rights to economic resources, as well as access to basic services, ownership, and control over land and other forms"
	+ " of property, inheritance, natural resources, appropriate new technology and financial services, including microfinance")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="5",body="By 2030, Build the resilience of the poor and those in vulnerable situations and"
	+ " reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="A",body="Ensure significant mobilization of resources from a variety of sources, including through enhanced"
	+ " development cooperation, in order to provide adequate and predictable means for developing countries, in particular least developed countries,"
	+ " to implement programmes and policies to end poverty in all its dimensions")
db.session.add(goal)
goal = Sdg_goals(goal_id="1",subgoal_id="B",body="Create sound policy frameworks at the national, regional and international levels, based on pro-poor"
	+ " and gender-sensitive development strategies, to support accelerated investment in poverty eradication actions")
db.session.add(goal)


goal = Sdg_goals(goal_id="2",subgoal_id="title",body="Zero Hunger")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="0",body="End hunger, achieve food security and improved nutrition, and promote sustainable agriculture")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="1",body="By 2030, end hunger and ensure access by all people, in particular the poor and people in vulnerable"
	+ " situations, including infants, to safe, nutritious and sufficient food all year round")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="2",body="By 2030, end all forms of malnutrition, including achieving, by 2025, the internationally agreed targets"
	+ " on stunting and wasting in children under 5 years of age, and address the nutritional needs of adolescent girls, pregnant and lactating women and older persons")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="3",body="By 2030, double the agricultural productivity and incomes of small-scale food producers, in particular"
	+ " women, indigenous peoples, family farmers, pastoralists and fishers, including through secure and equal access to land, other productive resources"
	+ " and inputs, knowledge, financial services, markets and opportunities for value addition and non-farm employment")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="4",body="By 2030, ensure sustainable food production systems and implement resilient agricultural practices that"
	+ " increase productivity and production, that help maintain ecosystems, that strengthen capacity for adaptation to climate change, extreme weather, drought,"
	+ " flooding and other disasters and that progressively improve land and soil quality")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="5",body="By 2020, maintain the genetic diversity of seeds, cultivated plants and farmed and domesticated animals"
	+ " and their related wild species, including through soundly managed and diversified seed and plant banks at the national, regional and international"
	+ " levels, and promote access to and fair and equitable sharing of benefits arising from the utilization of genetic resources and associated traditional"
	+ " knowledge, as internationally agreed")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="A",body="Increase investment, including through enhanced international cooperation, in rural infrastructure,"
	+ " agricultural research and extension services, technology development and plant and livestock gene banks in order to enhance agricultural productive"
	+ " capacity in developing countries, in particular least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="B",body="Correct and prevent trade restrictions and distortions in world agricultural markets, including through"
	+ " the parallel elimination of all forms of agricultural export subsidies and all export measures with equivalent effect, in accordance with the mandate"
	+ " of the Doha Development Round")
db.session.add(goal)
goal = Sdg_goals(goal_id="2",subgoal_id="C",body="Adopt measures to ensure the proper functioning of food commodity markets and their derivatives and facilitate"
	+ " timely access to market information, including on food reserves, in order to help limit extreme food price volatility")
db.session.add(goal)


goal = Sdg_goals(goal_id="3",subgoal_id="title",body="Good Health and Well Being")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="0",body="Ensure healthy lives and promote well-being for all at all costs")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="1",body="By 2030, reduce the global maternal mortality ratio to less than 70 per 100,000 live births")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="2",body="By 2030, end preventable deaths of newborns and children under 5 years of age, with all countries aiming"
	+ " to reduce neonatal mortality to at least as low as 12 per 1,000 live births and under-5 mortality to at least as low as 25 per 1,000 live births")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="3",body="By 2030, end the epidemics of AIDS, tubercolosis, malaria and neglected tropical diseases and combat"
	+ " hepatitis, water-borne diseases and other communicable diseases")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="4",body="By 2030, reduce by one third premature mortality from non-communicable diseases through prevention"
	+ " and treatment and promote mental health and well-being")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="5",body="Strengthen the prevention and treatment of substance abuse, including narcotic drug abuse and"
	+ " harmful use of alcohol")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="6",body="By 2020, halve the number of global deaths and injuries from road traffic accidents")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="7",body="By 2030, ensure universal access to sexual and reproductive health-care services, including for family"
	+ " planning, information and education, and the integration of reproductive health into national strategies and programmes")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="8",body="Achieve universal health coverage, including financial risk protection, access to quality essential"
	+ " health-care services and access to safe, effective, quality and afforfable essential medicines and vaccines for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="9",body="By 2030, substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water"
	+ " and soil pollution and contamination")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="A",body="Strengthen the implementation of the World Health Organization Framework Convention on Tobacco Control"
	+ " in all countries, as appropriate")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="B",body="Support the research and development of vaccines and medicines for the communicable and non-communicable"
	+ " diseases that primarily affect developing countries, provide access to affordable essential medicines and vaccines, in accordance with the Doha"
	+ " Declaration on the TRIPS Agreement and Public Health, which affirms the right of developing countries to use to the full the provisions in the"
	+ " Agreement on Trade-Related Aspects of Intellectual Property Rights regarding flexibilities to protect public health, and, in particular, provide"
	+ " access to medicines for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="C",body="Substantially increase health financing and the recruitment, development, training and retention of"
	+ " the health workforce in developing countries, especially in least developed countries and small island developing States")
db.session.add(goal)
goal = Sdg_goals(goal_id="3",subgoal_id="D",body="Strengthen the capacity of all countries, in particular developing countries, for early warning,"
	+ " risk reduction and management of national and global health risks")
db.session.add(goal)


goal = Sdg_goals(goal_id="4",subgoal_id="title",body="Quality Education")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="0",body="Ensure inclusive and equitable quality education and promote life-long learning opportunities for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="1",body="By 2030, ensure that all girls and boys complete free, equitable and quality primary and secondary"
	+ " education leading to relevant and effective learning outcomes")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="2",body="By 2030, ensure that all girls and boys have access to quality early childhood development, care"
	+ " and pre-primaryeducation so that they are ready for primary education")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="3",body="By 2030, ensure equal access for all women and men to affordable and quality technical, vocational"
	+ " and tertiary education, including university")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="4",body="By 2030, substantially increase the number of youth and adults who have relevant skills, including"
	+ " technical and vocational skills, for employment, decent jobs and entrepreneurship")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="5",body="By 2030, eliminate gender disparities in education and ensure equal access to all levels of education"
	+ " and vocational training for the vulnerable, including persons with disabilities, indigenous peoples and children in vulnerable situations")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="6",body="By 2030, ensure that all youth and a substantial proportion of adults, both men and women,"
	+ " achieve literacy and numeracy")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="7",body="By 2030, ensure that all learners acquire the knowledge and skills needed to promote sustainable"
	+ " development, including, among others, through education for sustainable development and sustainable lifestyles, human rights, gender equality,"
	+ " promotion of a culture of peace and non-violence, global citizenship and appreciation of cultural diversity and of culture's contribution to sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="A",body="Build and upgrade education facilities that are child, disability and gender sensitive and provide safe,"
	+ " non-violent, inclusive and effective learning environments for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="B",body="By 2020, substantially expand globally the number of scholarships available to developing countries, in"
	+ " particular least developed countries, small island developing States and African countries, for enrolment in higher education, including vocational"
	+ " training and information and communications technology, technical, engineering and scientific programmes, in developed countries and other developing countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="4",subgoal_id="C",body="By 2030, substantially increase the supply of qualified teachers, including through international cooperation"
	+ " for teacher training in developing countries, especially least developed countries and small island developing States")
db.session.add(goal)

goal = Sdg_goals(goal_id="5",subgoal_id="title",body="Gender Equality")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="0",body="Achieve gender equality and empower all women and girls")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="1",body="End all forms of discrimination against all women and girls everywhere")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="2",body="Eliminate all forms of violence againsta all women and girls in the public and private spheres, including"
	+ " trafficking and sexual and other types of exploitation")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="3",body="Eliminate all harmful practices, such as child, early and forced marriage and female genital mutilation")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="4",body="Recognize and value unpaid care and domestic work through the provision of public services, infrastructure"
	+ " and social protection policies and the promotion of shared responsibility within the household and the family as nationally appropriate")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="5",body="Ensure women's full and effective participation and equal opportunities for leadership at all levels"
	+ " of decision-making in political, economic and public life")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="6",body="Ensure universal access to sexual and reproductive health and reproductive rights as agreed in accordance"
	+ " with the Programme of Action of the International Conference on Population and Development and the Beijing Platform for Action and the outcome documents"
	+ " of their review conferences")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="A",body="Undertake reforms to give women equal rights to economic resources, as well as access to ownership and control"
	" over land and other forms of property, financial services, inheritance and natural resources, in accordance with national laws")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="B",body="Enhance the use of enabling technology, in particular information and communications technology, to promote"
	+ " the empowerment of women")
db.session.add(goal)
goal = Sdg_goals(goal_id="5",subgoal_id="C",body="Adopt and strengthen sound policies and enforceable legislation for the promotion of gender equality"
	+ " and the empowerment of all women and girls at all levels")
db.session.add(goal)


goal = Sdg_goals(goal_id="6",subgoal_id="title",body="Clean Water and Sanitation")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="0",body="Ensure availability and sustainable management of water and sanitation for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="1",body="By 2030, achieve universal and equitable access to safe and affordable drinking water for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="2",body="By 2030, achieve success to adequate and equitable sanitation and hygiene for all and end open defecation,"
	+ " paying special attention to the needs of women and girls and those in vulnerable situations")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="3",body="By 2030, improve water quality by reducing pollution, eliminating dumping and minimizing release of hazardous"
	+ " chemicals and materials, having the proportion of untreated wastewater and substantially increasing recycling and safe reuse globally")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="4",body="By 2030, substantially increase water-use efficiency across all sectors and ensure sustainable withdrawals"
	+ " and supply of freshwater to address water scarcity and substantially reduce the number of people suffering from water scarcity")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="5",body="By 2030, implement integrated water resources management at all levels, including through transboundary"
	+ " cooperation as appropriate")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="6",body="By 2020, protect and restore water-related ecosystems, including mountains, forests, wetlands, rivers,"
	+ " aquifers and lakes")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="A",body="By 2030, expand international cooperation and capacity-building support to developing countries in water-"
	+ " and sanitation-related activities and programmes, including water harvesting, desalination, water efficiency, wastewater treatment, recycling and reuse technologies")
db.session.add(goal)
goal = Sdg_goals(goal_id="6",subgoal_id="B",body="Support and strengthen the participation of local communities in improving water and sanitation management")
db.session.add(goal)


goal = Sdg_goals(goal_id="7",subgoal_id="title",body="Affordable and Clean Energy")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="0",body="Ensure access to affordable, reliable, sustainable, and modern energy for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="1",body="By 2030, ensure universal access to affordable, reliable and modern energy services")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="2",body="By 2030, increase substantially share of renewable energy in the global energy mix")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="3",body="By 2030, double the global rate of improvement in energy efficiency")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="A",body="By 2030, enhance international cooperation to facilitate access to clean energy research and technology,"
	+ " including renewable energy, energy efficiency and advanced and cleaner fossil-fuel technology, and promote investment in energy infrastructure and clean energy technology")
db.session.add(goal)
goal = Sdg_goals(goal_id="7",subgoal_id="B",body="By 2030, expand infrastructure and upgrade technology for supplying modern and sustainable energy services"
	+ " for all in developing countries, in particular least developed countries, small island developing States, and land-locked developing countries, in"
	+ " accordance with their respective programmes of support")
db.session.add(goal)


goal = Sdg_goals(goal_id="8",subgoal_id="title",body="Decent Work and Economic Growth")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="0",body="Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="1",body="Sustain per capita economic growth in accordance with national circumstances and, in particular, at least"
	+ " 7 per cent gross domestic product growth per annum in the least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="2",body="Achieve higher levels of economic productivity through diversification, technological upgrading and innovation,"
	+ " including through a focus on high-value added and labour-intensive sectors")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="3",body="Promote development-oriented policies that support productive activities, decent job creation, entrepreneurship,"
	+ " creativity and innovation, and encourage the formalization and growth of micro-, small- and medium-sized enterprises, including through access to financial services")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="4",body="Improve progressively, through 2030, global resource efficiency in consumption and production and endeavour"
	+ " to decouple economic growth from environmental degradation, in accordance with the 10-year framework of programmes on sustainable consumption and production,"
	+ " with developed countries taking the lead")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="5",body="By 2030, achieve full and productive employment and decent work for all women and men, including for young people"
	+ " and persons with disabilities, and equal pay for work of equal value")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="6",body="By 2020, substantially reduce the proportion of youth not in employment, education or training")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="7",body="Take immediate and effective measures to eradicate forced labour, end modern slavery and human trafficking"
	+ " and secure the prohibition and elimination of the worst forms of child labour, including recruitment and use of child soldiers, and by 2025 end child labour in all its forms")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="8",body="Protect labour rights and promote safe and secure working environments for all workers, including migrant"
	+ " workers, in particular women migrants, and those in precarious employment")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="9",body="By 2030, devise and implement policies to promote sustainable tourism that creates jobs and promotes"
	+ " local culture and products")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="10",body="Strengthen the capacity of domestic financial institutions to encourage and expand access to banking,"
	+ " insurance and financial services for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="8",subgoal_id="A",body="Increase Aid for Trade support for developing countries, in particular least developed countries, including"
	+ " through the Enhanced Integrated Framework for Trade-Related Technical Assistance to Least Developed Countries")
db.session.add(goal)
goal = Sdg_goals(
	goal_id="8",
	subgoal_id="B",
	body="By 2020, develop and operationalize a global strategy for youth employment and implement the Global Jobs"
	+ " Pact of the International Labour Organization"
)
db.session.add(goal)


goal = Sdg_goals(goal_id="9",subgoal_id="title",body="Industry, Innovation and Infrastructure")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="0",body="Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="1",body="Develop quality, reliable, sustainable and resilient infrastructure, including regional and transborder"
	+ " infrastructure, to support economic development and human well-being, with a focus on affordable and equitable access for all")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="2",body="Promote inclusive and sustainable industrialization and, by 2030, significantly raise industry's share of"
	+ " employment and gross domestic product, in line with national circumstances, and double its share in least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="3",body="Increase the access of small-scale industrial and other enterprises, in particular in developing countries,"
	+ " to financial services, including affordable credit, and their integration into value chains and markets")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="4",body="By 2030, upgrade infrastructure and retrofit industries to make them sustainable, with increased resource-use"
	+ " efficiency and greater adoption of clean and environmentally sound technologies and industrial processes, with all countries taking action in"
	+ " accordance with their respective capabilities")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="5",body="Enhance scientific research, upgrade the technological capabilities of industrial sectors in all countries,"
	+ " in particular developing countries, including, by 2030, encouraging innovation and substantially increasing the number of research and development"
	+ " workers per 1 million people and public and private and development spending")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="A",body="Facilitate sustainable and resilient infrastructure development in developing countries through enhanced"
	+ " financial, technological and technical support to African countries, least developed countries, landlocked developing countries and small island developing States")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="B",body="Support domestic technology development, research and innovation in developing countries, including by"
	+ " ensuring a conducive policy environment for, inter alia, industrial diversification and value addition to commodities")
db.session.add(goal)
goal = Sdg_goals(goal_id="9",subgoal_id="C",body="Significantly increase access to information and communications technology and strive to provide universal"
	+ " and affordable access to the Internet in least developed countries by 2020")
db.session.add(goal)



goal = Sdg_goals(goal_id="10",subgoal_id="title",body="Reduced Inequality")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="0",body="Reduce inequality within and among countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="1",body="By 2030, progressively achieve and sustain income growth of the bottom 40 per cent of the population"
	+ " at a rate higher than the national average")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="2",body="By 2030, empower and promote the social, economic and political inclusion of all, irrespective of age,"
	+ " sex, disability, race, ethnicity, origin, religion or economic or other status")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="3",body="Ensure equal opportunity and reduce inequalities of outcome, including by eliminating discriminatory"
	+ " laws, policies and practices and promoting appropriate legislation, policies and action in this regard")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="4",body="Adopt policies, especially fiscal, wage and social protection policies, and progressively achieve greater equality")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="5",body="Improve the regulation and monitoring of global financial markets and institutions and strengthen"
	+ " the implementation of such regulations")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="6",body="Ensure enhanced representation and voice for developing countries in decision-making in global international"
	+ " economic and financial institutions in order to deliver more effective, credible, accountable and legitimate institutions")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="7",body="Facilitate orderly, safe, regular and responsible migration and mobility of people, including through the"
	+ " implementation of planned and well-managed migration policies")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="A",body="Implement the principle of special and differential treatment for developing countries, in particular"
	+ " least developed countries, in accordance with World Trade Organization agreements")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="B",body="Encourage official development assistance and financial flows, including foreign direct investment, to"
	+ " States where the need is greatest, in particular least developed countries, African countries, small island developing States and landlocked"
	+ " developing countries, in accordance with their national plans and programmes")
db.session.add(goal)
goal = Sdg_goals(goal_id="10",subgoal_id="C",body="By 2030, reduce to less than 3 per cent the transaction costs of migrant remittances and eliminate remittance"
	+ " corridors with costs higher than 5 per cent")
db.session.add(goal)


goal = Sdg_goals(goal_id="11",subgoal_id="title",body="Sustainable Cities and Communities")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="0",body="Make cities and human settlements inclusive, safe, resilient and sustainable")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="1",body="By 2030, ensure access for adequate, safe and affordable housing and basic services and upgrade slums")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="2",body="By 2030, provide access to safe, affordable, accessible and sustainable transport systems for all,"
	+ " improving road safety, notably by expanding public transport, with special attention to the needs of those in vulnerable situations, women,"
	+ " children, persons with disabilities and older persons")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="3",body="By 2030, enhance inclusive and sustainable urbanization and capacity for participatory, integrated"
	+ " and sustainable human settlement planning and management in all countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="4",body="Strengthen efforts to protect and safeguard the world's cultural and natural heritage")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="5",body="By 2030, significantly reduce the number of deaths and the number of people affected and substantially"
	+ " decrease the direct economic losses relative to global gross domestic product caused by disasters, including water-related disasters, with a focus"
	+ " on protecting the poor and people in vulnerable situations")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="6",body="By 2030, reduce the adverse per capita environmental impact of cities, including by paying special"
	+ " attention to air quality and municipal and other waste management")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="7",body="By 2030, provide universal access to safe, inclusive and accessible, green and public spaces, in"
	+ " particular for women and children, older persons and persons with disabilities")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="A",body="Support positive economic, social and environmental links between urban, per-urban and rural areas"
	+ " by strengthening national and regional development planning")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="B",body="By 2020, substantially increase the number of cities and human settlements adopting and implementing"
	+ " integrated policies and plans toward inclusion, resource efficiency, mitigation and adaptation to climate change, resilience to disasters, and"
	+ " develop and implement, in line with the Sendai Framework for Disaster Risk Reduction 2015-2030, holistic disaster risk management at all levels")
db.session.add(goal)
goal = Sdg_goals(goal_id="11",subgoal_id="C",body="Support least developed countries, including through financial and technical assistance, in building"
	+ " sustainable and resilient buildings utilizing local materials")
db.session.add(goal)


goal = Sdg_goals(goal_id="12",subgoal_id="title",body="Responsible Consumption and Production")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="0",body="Ensure sustainable consumption and production patterns")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="1",body="Implement the 10-year framework of programmes on sustainable consumption and production, all countries"
	+ " taking action, with developed countries taking the lead, taking into account the development and capabilities of developing countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="2",body="By 2030, achieve the sustainable management and efficient use of natural resources")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="3",body="By 2030, halve per capita global food waste at the retail and consumer levels and reduce food losses"
	+ " along production and supply chains, including post-harvest losses")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="4",body="By 2020, achieve the environmentally sound management of chemicals and all wastes throughout their life cycle,"
	+ " in accordance with agreed international frameworks and significantly reduce their release to air, water and soil in order to minimize their adverse"
	+ " impacts on human health and the environment")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="5",body="By 2030, substantially reduce waste generation through prevention, reduction, recycling and reuse")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="6",body="Encourage companies, especially large and transnational companies, to adopt sustainable practices"
	+ " and to integrate sustainability information into their reporting cycle")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="7",body="Promote public procurement practices that are sustainable, in accordance with national policies and priorities")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="8",body="By 2030, ensure that people everywhere have the relevant information and awareness for sustainable"
	+ " development and lifestyles in harmony with nature")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="A",body="Support developing countries to strengthen their scientific and technological capacity to move towards more"
	+ " sustainable patterns of consumption and production")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="B",body="Develop and implement tools to monitor sustainable development impacts for sustainable tourism that"
	+ " creates jobs and promotes local culture and products")
db.session.add(goal)
goal = Sdg_goals(goal_id="12",subgoal_id="C",body="Rationalize inefficient fossil-fuel subsidies that encourage wasteful consumption by removing market"
	+ " distortions, in accordance with national circumstances, including by restructuring taxation and phasing out those harmful subsidies, where they"
	+ " exist, to relfect their environmental impacts, taking fully into account the specific needs and conditions of developing countries and minimizing"
	+ " the possible adverse impacts on their development in a manner that protects the poor and the affected communities")
db.session.add(goal)


goal = Sdg_goals(goal_id="13",subgoal_id="title",body="Climate Action")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="0",body="Take urgent action to combat climate change and its impacts")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="1",body="Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="2",body="Integrate climate change measures into national policies, strategies and planning")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="3",body="Improve education, awareness-raising and human and institutional capacity on climate change mitigation,"
	+ " adaptation, impact reduction and early warning")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="A",body="Implement the commitment undertaken by developed-country parties to the United Nations Framework Convention"
	+ " on Climate Change to a goal of mobilizing jointly $100 billion annually by 2020 from all sources to address the needs of developing countries in the context"
	+ " of meaningful mitigation actions and transparency on implementation and fully operationalize the Green Climate Fund through its capitalization as soon as possible")
db.session.add(goal)
goal = Sdg_goals(goal_id="13",subgoal_id="B",body="Promote mechanisms for raising capacity for effective climate change-related planning and management in"
	+ " least developed countries and small island developing States, including focusing on women, youth and local and marginalized countries")
db.session.add(goal)



goal = Sdg_goals(goal_id="14",subgoal_id="title",body="Life Below Water")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="0",body="Conserve and sustainably use the oceans, seas and marine resources for sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="1",body="By 2025, prevent and significantly reduce marine pollution of all kings, in particular from land-based"
	+ " activities, including marine debris and nutrient pollution")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="2",body="By 2020, sustainably manage and protect marine and coastal ecosystems to avoid significant adverse"
	+ " impacts, including by strengthening their resilience, and take action for their restoration in order to achieve healthy and productive oceans")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="3",body="Minimize and address the impacts of ocean acidification, including through enhanced scientific cooperation"
	+ " at all levels")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="4",body="By 2020, effectively regulate harvesting and end overfishing, illegal, unreported and unregulated fishing"
	+ " and destructive fishing practices and implement science-based management plans, in order to restore fish stocks in the shortest time feasible, at"
	+ " least to levels that can produce maximum yet sustainable yield as determined by their biological characteristics")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="5",body="By 2020, conserve at least 10 per cent of coastal and marine areas, consistent with national and international"
	+ " law and based on the best available scientific information")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="6",body="By 2020, prohibit certain forms of fisheries subsidies which contribute to overcapacity and overfishing,"
	+ " eliminate subsidies which contribute to illegal, unreported and unregulated fishing and refrain from introducing new such subsidies, recognizing"
	+ " that appropriate and effective special and differential treatment for developing and least developed countries should be an integral part of the"
	+ " World Trade Organization fisheries subsidies negotiation")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="7",body="By 2030, increase the economic benefits to Small Island developing States and least developed countries"
	+ " from the sustainable use of marine resources, including through sustainable management of fisheries, aquaculture and tourism")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="A",body="Increase scientific knowledge, develop research capacity and transfer marine technology, taking into"
	+ " account the Intergovernmental Oceanographic Commission Criteria and Guidelines on the Transfer of Marine Technology, in order to improve ocean"
	+ " health and to enhance the contribution of marine biodiversity to the development of developing countries, in particular small island developing"
	+ " States and least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="B",body="Provide access for small-scale artisanal fishers to marine resources and markets")
db.session.add(goal)
goal = Sdg_goals(goal_id="14",subgoal_id="C",body="Enhancr the conservation and sustainable use of oceans and their resources by implementing international"
	+ " law as reflected in UNICLOS, which provides the legal framework for the conservation and sustainable use of oceans and their resources, as recalled"
	+ " in paragraph 158 of The Future We Want")
db.session.add(goal)


goal = Sdg_goals(goal_id="15",subgoal_id="title",body="Life on Land")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="0",body="Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat"
	+ " desertification, and halt and reverse land degradation and halt biodiversity loss")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="1",body="By 2020, ensure the conservation, restoration and sustainable use of terrestrial and inland freshwater"
	+ " ecosystems and their services, in particular forests, wetlands, mountains and drylands, in line with obligations under international agreements")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="2",body="By 2020, promote the implementation of sustainable management of all types of forests, halt deforestation,"
	+ " restore degraded forests and substantially increase afforestation and reforestation globally")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="3",body="By 2030, combat desertification, restore degraded land and soil, including land affected by desertification,"
	+ " drought and floods, and strive to achieve a land degradation-neutral world")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="4",body="By 2030, ensure the conservation of mountain ecosystems, including their biodiversity, in order to enhance"
	+ " their capacity to provide benefits that are essential to sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="5",body="Take urgent and significant action to reduce the degradation of natural habitats, halt the loss of biodiversity"
	+ " and, by 2020, protect and prevent the extinction of threatened species")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="6",body="Promote fair and equitable sharing of the benefits arising from the utilization of genetic resources and"
	+ " promote appropriate access to such resources, as internationally agreed")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="7",body="Take urgent action to end poaching and trafficking of protected species of flora and fauna and address"
	+ " both demand and supply of illegal wildlife products")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="8",body="By 2020, introduce measures to prevent the introduction and significantly reduce the impact of invasive"
	+ " alien species on land and water ecosystems and control or eradicate the priority species")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="9",body="By 2020, integrate ecosystem and biodiversity values into national and local planning, development processes,"
	+ " poverty reduction strategies and accounts")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="A",body="Mobilize and significantly increase financial resources from all sources to conserve and sustainably"
	+ " use biodiversity and ecosystems")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="B",body="Mobilize significant resources from all sources and at all levels to finance sustainable forest management"
	+ " and provide adequate incentives to developing countries to advance such management, including for conservation and reforestation")
db.session.add(goal)
goal = Sdg_goals(goal_id="15",subgoal_id="C",body="Enhance global support for efforts to combat poaching and trafficking of protected species, including"
	+ " by increasing the capacity of local communities to pursue sustainable livelihood opportunities")
db.session.add(goal)


goal = Sdg_goals(goal_id="16",subgoal_id="title",body="Peace and Justice Strong Institutions")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="0",body="Promote peaceful and inclusive societies for sustainable development, provide access to justice for all"
	+ " and build effective, accountable and inclusive institutions at all levels")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="1",body="Significantly reduce all forms of violence and related death rates everywhere")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="2",body="End abuse, exploitation, trafficking and all forms of violence against and torture of children")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="3",body="Promote the rule of law at the national and international levels and ensure equal access to justice for alll")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="4",body="By 2030, significantly reduce illicit financial and arms flows, strengthen the recovery and return of"
	+ " stolen assets and combat all forms of organized crime")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="5",body="Substantially reduce corruption and bribery in all their forms")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="6",body="Develop effective, accountable and transparent institutions at all levels")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="7",body="Ensure responsive, inclusive, participatory and representative decision-making at all levels")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="8",body="Broaden and strengthen the participation of developing countries in the institutions of global governance")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="9",body="By 2030, provide legal identity for all, including birth registration")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="10",body="Ensure public access to information and protect fundamental freedoms, in accordance with national legislation"
	+ " and international agreements")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="A",body="Strengthen relevant national institutions, including through international cooperation, for building"
	+ " capacity at all levels, in particular in developing countries, to prevent violence and combat terrorism and crime")
db.session.add(goal)
goal = Sdg_goals(goal_id="16",subgoal_id="B",body="Promote and enforce non-discriminatory laws and policies for sustainable development")
db.session.add(goal)


goal = Sdg_goals(goal_id="17",subgoal_id="title",body="Partnerships to achieve the Goal")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="0",body="Strengthen the means of implementation and revitalize the global partnership for sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="1",body="Strengthen domestic resource mobilization, including through international support to developing countries,"
	+ " to improve domestic capacity for tax and other revenue collection")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="2",body="Developed countries to implement fully their official development assistance commitments, including the"
	+ " commitment by many developed countries to achieve the target of 0.7 per cent of ODA/GNI to developing countries and 0.15 to 0.20 per cent of ODA/GNI"
	+ " to least developed countries; ODA providers are encouraged to consider setting a target to provide at least 0.20 per cent od ODA/GNI to least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="3",body="Mobilize additional financial resources for developing countries from multiple sources")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="4",body="Assist developing countries in attaining long-term debt sustainability through coordinated policies aimed"
	+ " at fostering debt financing. debt relief and debt restructuring, as appropriate, and address the external debt of highly indebted poor countries to reduce debt distress")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="5",body="Adopt and implement investment promotion regimes for least developed countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="6",body="Enhance North-South, South-South and triangular regional and international cooperation on and access to"
	+ " science, technology and innovation and enhance knowledge sharing on mutually agreed terms, including through improved coordination among existing mechanisms,"
	+ " in particular at the United Nations level, and through a global technology facilitation mechanism")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="7",body="Promote the development, transfer, dissemination and diffusion of environmentally sound technologies"
	+ " to developing countries on favourable terms, including on concessional and preferential terms, as mutually agrees")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="8",body="Fully operationalize the technology bank and science, technology and innovation capacity-building mechanism"
	+ " for least developed countries by 2017 and enhance the use of enabling technology, in particular information and communications technology")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="9",body="Enhance international support for implementing effective and targeted capacity-building in developing"
	+ " countries to support national plans to implement all the sustainable development goals, including through North-South, South-South and triangular cooperation")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="10",body="Promote a universal, rules-based, open, non-discriminatory and equitable multilateral trading system"
	+ " under the World Trade Organization, including through the conclusion of negotiations under its Doha Development Agenda")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="11",body="Significantly increase the exports of developing countries, in particular with a view to doubling the"
	+ " least developed countries' share of global exports by 2020")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="12",body="Realize timely implementation of duty-free and quota-free market access on a lasting basis for all least"
	+ " developed countries, consistent with World Trade Organization decisions, including by ensuring that preferential rules of origin applicable to imports"
	+ " from least developed countries are transparent and simple, and contribute to facilitating market access")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="13",body="Enhance global macroeconomic stability, including through policy coordination and policy coherence")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="14",body="Enhance policy coherence for sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="15",body="Respect each country's policy space and leadership to establish and implement policies for poverty"
	+ " eradication and sustainable development")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="16",body="Enhance the global partnership for sustainable development, complemented by multi-stakeholder partnerships"
	+ " that mobilize and share knowledge, expertise, technology and financial resources, to support the achievement of the sustainable development goals in"
	+ " all countries, in particular developing countries")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="17",body="Encourage and promote effective public, public-private and civil society partnerships, building on the"
	+ " experience and resourcing strategies of partnerships")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="18",body="By 2020, enhance capacity-building support to developing countries, including for least developed countries"
	+ " and small island developing States, to increase significantly the availability of high-quality, timely and reliable data disaggregated by income, gender,"
	+ " age, race, enthnicity, migratory status, disability, geographic location and other characteristics relevant in national contexts")
db.session.add(goal)
goal = Sdg_goals(goal_id="17",subgoal_id="19",body="By 2030, build on existing initiatives to develop measurements of progress on sustainable development that"
	+ " complement gross domestic product, and support statistical capacity-building in developing countries")
db.session.add(goal)

db.session.commit()