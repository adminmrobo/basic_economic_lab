# 경제학 표준 색인어 대응표

이 연구실의 개념·용어를 경제학 표준 어휘 세 가지에 연결한 표입니다. 페이지의 「지식 색인」과 「온톨로지·서지 꾸러미」(JSON-LD의 `skos:closeMatch`·`skos:broadMatch`·`skos:relatedMatch`, `dct:subject`), `KG_00_registry.json`에 같은 값이 들어 있습니다.

- **JEL**: 미국경제학회 JEL 분류. 코드와 제목은 [AEA JEL 목록](https://www.aeaweb.org/econlit/jelCodes.php?view=jel)에서 확인했고, 개념마다 가장 가까운 분류를 배정했습니다(`dct:subject`).
- **STW**: ZBW 「STW Thesaurus for Economics」. 조회 서비스에서 ID와 라벨을 확인했습니다. 「같은 개념」은 closeMatch, 「상위어」는 STW 쪽이 더 넓은 개념(broadMatch), 「관련어」는 relatedMatch입니다.
- **Wikidata**: 각 STW 항목 페이지에 적힌 대응만 옮겼습니다. STW에 대응이 없으면 비워 두었습니다.
- STW에서 찾지 못한 4개(희소성, 상충관계, 경제재, 무료재)는 JEL만 붙였습니다.

확인일: 2026-11-24

| 이 연구실 개념 | 영문 | 쪽 | JEL | STW | 관계 | Wikidata |
|---|---|---|---|---|---|---|
| 유인 | incentive | 01 | D01 | [Incentives](https://zbw.eu/stw/descriptor/19533-5) | 같은 개념 | [Q1414816](https://www.wikidata.org/wiki/Q1414816) |
| 한계편익 | marginal benefit | 01 | D01 | [Marginal analysis](https://zbw.eu/stw/descriptor/19218-6) | 상위어 | [Q18460372](https://www.wikidata.org/wiki/Q18460372) |
| 한계비용 | marginal cost | 01 | D01 D24 | [Marginal costs](https://zbw.eu/stw/descriptor/20881-0) | 같은 개념 | [Q382444](https://www.wikidata.org/wiki/Q382444) |
| 한계적 판단 | thinking at the margin | 01, 05m | D01 | [Marginal analysis](https://zbw.eu/stw/descriptor/19218-6) | 같은 개념 | [Q18460372](https://www.wikidata.org/wiki/Q18460372) |
| 기회비용 | opportunity cost | 01, 05m | D01 | [Opportunity cost](https://zbw.eu/stw/descriptor/10052-3) | 같은 개념 | [Q185715](https://www.wikidata.org/wiki/Q185715) |
| 희소성 | scarcity | 01, 05m | A10 D01 | — | — | — |
| 매몰비용 | sunk cost | 01 | D01 | [Sunk costs](https://zbw.eu/stw/descriptor/19432-4) | 같은 개념 | [Q958242](https://www.wikidata.org/wiki/Q958242) |
| 경제재 | economic good | 01 | D01 | — | — | — |
| 경제적 이윤 | economic profit | 01 | D21 | [Profit](https://zbw.eu/stw/descriptor/12275-1) | 상위어 | [Q26911](https://www.wikidata.org/wiki/Q26911) |
| 명시적 비용 | explicit cost | 01 | D24 | [Costs](https://zbw.eu/stw/descriptor/10011-3) | 상위어 | [Q240673](https://www.wikidata.org/wiki/Q240673) |
| 무료재 | free good | 01 | D01 | — | — | — |
| 암묵적 비용 | implicit cost | 01 | D24 | [Opportunity cost](https://zbw.eu/stw/descriptor/10052-3) | 상위어 | [Q185715](https://www.wikidata.org/wiki/Q185715) |
| 이전소득 | transfer income | 01 | H55 | [Social security benefits](https://zbw.eu/stw/descriptor/11569-3) | 관련어 | [Q59284985](https://www.wikidata.org/wiki/Q59284985) |
| 소비함수 | consumption function | 02 | E21 | [Consumption theory](https://zbw.eu/stw/descriptor/10181-6) | 상위어 | [Q1002494](https://www.wikidata.org/wiki/Q1002494) |
| 경제성장 | economic growth | 02 | O40 O47 | [Economic growth](https://zbw.eu/stw/descriptor/10414-2) | 같은 개념 | [Q189833](https://www.wikidata.org/wiki/Q189833) |
| 경제모형 | economic model | 02, 05m | B41 | [Economic model](https://zbw.eu/stw/descriptor/10065-1) | 같은 개념 | [Q2180497](https://www.wikidata.org/wiki/Q2180497) |
| 거시경제학 | macroeconomics | 02 | A10 | [Macroeconomics](https://zbw.eu/stw/descriptor/10249-5) | 같은 개념 | [Q39680](https://www.wikidata.org/wiki/Q39680) |
| 미시경제학 | microeconomics | 02 | A10 | [Microeconomics](https://zbw.eu/stw/descriptor/10144-5) | 같은 개념 | [Q39072](https://www.wikidata.org/wiki/Q39072) |
| 규범경제학 | normative economics | 02 | B41 D63 | [Normative economics](https://zbw.eu/stw/descriptor/19989-4) | 같은 개념 | [Q26086](https://www.wikidata.org/wiki/Q26086) |
| 실증경제학 | positive economics | 02 | B41 | [Positive economics](https://zbw.eu/stw/descriptor/20022-6) | 같은 개념 | [Q26110](https://www.wikidata.org/wiki/Q26110) |
| 실증경제학과 규범경제학 | positive vs normative economics | 02, 05m | B41 | [Normative economics](https://zbw.eu/stw/descriptor/19989-4) | 같은 개념 | [Q26086](https://www.wikidata.org/wiki/Q26086) |
| 생산가능곡선 | production possibility frontier | 02, 05m | D24 | [Technical efficiency](https://zbw.eu/stw/descriptor/10328-2) | 같은 개념 | [Q376791](https://www.wikidata.org/wiki/Q376791) |
| 가정 | assumption | 02 | B41 | [Economic model](https://zbw.eu/stw/descriptor/10065-1) | 상위어 | [Q2180497](https://www.wikidata.org/wiki/Q2180497) |
| 기회비용 체증 | increasing opportunity cost | 02 | D24 | [Opportunity cost](https://zbw.eu/stw/descriptor/10052-3) | 상위어 | [Q185715](https://www.wikidata.org/wiki/Q185715) |
| 한계소비성향 | marginal propensity to consume | 02 | E21 | [Consumption theory](https://zbw.eu/stw/descriptor/10181-6) | 상위어 | [Q1002494](https://www.wikidata.org/wiki/Q1002494) |
| 상충관계 | trade-off | 02 | D01 | — | — | — |
| 수요 | demand | 03, 05m | D11 | [Demand](https://zbw.eu/stw/descriptor/10013-6) | 같은 개념 | [Q4402708](https://www.wikidata.org/wiki/Q4402708) |
| 시장균형 | market equilibrium | 03, 05m | D40 | [Market equilibrium](https://zbw.eu/stw/descriptor/30553-4) | 같은 개념 | — |
| 공급 | supply | 03, 05m | D21 | [Supply](https://zbw.eu/stw/descriptor/10000-1) | 같은 개념 | [Q542869](https://www.wikidata.org/wiki/Q542869) |
| 보완재 | complements | 03 | D11 | [Complementary goods](https://zbw.eu/stw/descriptor/29965-5) | 같은 개념 | — |
| 초과수요 | excess demand | 03 | D40 | [Market equilibrium](https://zbw.eu/stw/descriptor/30553-4) | 상위어 | — |
| 초과공급 | excess supply | 03 | D40 | [Market equilibrium](https://zbw.eu/stw/descriptor/30553-4) | 상위어 | — |
| 열등재 | inferior good | 03 | D11 | [Inferior goods](https://zbw.eu/stw/descriptor/10178-2) | 같은 개념 | [Q588065](https://www.wikidata.org/wiki/Q588065) |
| 정상재 | normal good | 03 | D11 | [Income elasticity of demand](https://zbw.eu/stw/descriptor/10171-2) | 관련어 | [Q734113](https://www.wikidata.org/wiki/Q734113) |
| 수요량 | quantity demanded | 03 | D11 | [Demand](https://zbw.eu/stw/descriptor/10013-6) | 상위어 | [Q4402708](https://www.wikidata.org/wiki/Q4402708) |
| 공급량 | quantity supplied | 03 | D21 | [Supply](https://zbw.eu/stw/descriptor/10000-1) | 상위어 | [Q542869](https://www.wikidata.org/wiki/Q542869) |
| 대체재 | substitutes | 03 | D11 | [Substitute goods](https://zbw.eu/stw/descriptor/18129-3) | 같은 개념 | [Q312588](https://www.wikidata.org/wiki/Q312588) |
| 교차탄력성 | cross-price elasticity | 04 | D11 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 탄력성과 총수입 | elasticity and total revenue | 04, 05m | D11 D21 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 소득·교차·공급 탄력성 | income, cross-price and supply elasticity | 04, 05m | D11 D12 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 같은 개념 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 소득탄력성 | income elasticity | 04 | D12 | [Income elasticity of demand](https://zbw.eu/stw/descriptor/10171-2) | 같은 개념 | [Q734113](https://www.wikidata.org/wiki/Q734113) |
| 수요의 가격탄력성 | price elasticity of demand | 04, 05m | D11 D12 | [Price elasticity](https://zbw.eu/stw/descriptor/10055-4) | 같은 개념 | [Q3194154](https://www.wikidata.org/wiki/Q3194154) |
| 공급탄력성 | price elasticity of supply | 04 | D21 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 호 탄력성 | arc elasticity | 04 | D11 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 탄력적 | elastic | 04 | D11 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 비탄력적 | inelastic | 04 | D11 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 단위탄력적 | unit elastic | 04 | D11 | [Elasticity](https://zbw.eu/stw/descriptor/10036-1) | 상위어 | [Q223639](https://www.wikidata.org/wiki/Q223639) |
| 총수입 | total revenue | 04 | D21 | [Revenue](https://zbw.eu/stw/descriptor/12311-2) | 같은 개념 | [Q350205](https://www.wikidata.org/wiki/Q350205) |
| 가격상한제 | price ceiling | 05, 05m | D45 | [Price regulation](https://zbw.eu/stw/descriptor/10978-5) | 같은 개념 | [Q9305568](https://www.wikidata.org/wiki/Q9305568) |
| 가격하한제 | price floor | 05, 05m | J38 | [Price regulation](https://zbw.eu/stw/descriptor/10978-5) | 상위어 | [Q9305568](https://www.wikidata.org/wiki/Q9305568) |
| 조세의 귀착 | tax incidence | 05, 05m | H22 | [Tax incidence](https://zbw.eu/stw/descriptor/11692-4) | 같은 개념 | [Q2165871](https://www.wikidata.org/wiki/Q2165871) |
| 암시장 | black market | 05 | D45 | [Illicit trade](https://zbw.eu/stw/descriptor/10845-3) | 같은 개념 | [Q57262007](https://www.wikidata.org/wiki/Q57262007) |
| 경제적 귀착 | economic incidence | 05 | H22 | [Tax incidence](https://zbw.eu/stw/descriptor/11692-4) | 상위어 | [Q2165871](https://www.wikidata.org/wiki/Q2165871) |
| 최저임금 | minimum wage | 05 | J38 | [Minimum wage](https://zbw.eu/stw/descriptor/11328-4) | 같은 개념 | [Q186228](https://www.wikidata.org/wiki/Q186228) |
| 할당 | rationing | 05 | D45 | [Rationing](https://zbw.eu/stw/descriptor/11034-0) | 같은 개념 | [Q843478](https://www.wikidata.org/wiki/Q843478) |
| 법적 귀착 | statutory incidence | 05 | H22 | [Tax incidence](https://zbw.eu/stw/descriptor/11692-4) | 상위어 | [Q2165871](https://www.wikidata.org/wiki/Q2165871) |
| 조세의 전가 | tax shifting | 05 | H22 | [Tax incidence](https://zbw.eu/stw/descriptor/11692-4) | 같은 개념 | [Q2165871](https://www.wikidata.org/wiki/Q2165871) |
| 소비자잉여 | consumer surplus | 06, 11f | D61 | [Consumer surplus](https://zbw.eu/stw/descriptor/10180-1) | 같은 개념 | [Q361800](https://www.wikidata.org/wiki/Q361800) |
| 효율성 | efficiency | 06 | D61 | [Efficiency](https://zbw.eu/stw/descriptor/11039-4) | 같은 개념 | [Q1034411](https://www.wikidata.org/wiki/Q1034411) |
| 형평성 | equity | 06 | D63 | [Distributive justice](https://zbw.eu/stw/descriptor/10110-1) | 같은 개념 | [Q552284](https://www.wikidata.org/wiki/Q552284) |
| 시장실패 | market failure | 06 | D61 D62 | [Market failure](https://zbw.eu/stw/descriptor/11054-1) | 같은 개념 | [Q622657](https://www.wikidata.org/wiki/Q622657) |
| 생산자잉여 | producer surplus | 06, 11f | D61 | [Welfare economics](https://zbw.eu/stw/descriptor/10113-2) | 상위어 | [Q851147](https://www.wikidata.org/wiki/Q851147) |
| 가격차별 | price discrimination | 06 | D42 | [Price discrimination](https://zbw.eu/stw/descriptor/10215-1) | 같은 개념 | [Q835678](https://www.wikidata.org/wiki/Q835678) |
| 총잉여와 효율성 | total surplus and efficiency | 06, 11f | D61 | [Welfare economics](https://zbw.eu/stw/descriptor/10113-2) | 상위어 | [Q851147](https://www.wikidata.org/wiki/Q851147) |
| 지불용의 | willingness to pay | 06 | D11 | [Willingness to pay](https://zbw.eu/stw/descriptor/19210-1) | 같은 개념 | [Q140813](https://www.wikidata.org/wiki/Q140813) |
| 공급용의 | willingness to sell | 06 | D21 | [Willingness to pay](https://zbw.eu/stw/descriptor/19210-1) | 관련어 | [Q140813](https://www.wikidata.org/wiki/Q140813) |
| 사중손실 | deadweight loss | 07, 11f | H21 | [Excess burden](https://zbw.eu/stw/descriptor/11685-1) | 같은 개념 | [Q5419530](https://www.wikidata.org/wiki/Q5419530) |
| 탄력성과 사중손실 | elasticity and deadweight loss | 07, 11f | H21 | [Excess burden](https://zbw.eu/stw/descriptor/11685-1) | 같은 개념 | [Q5419530](https://www.wikidata.org/wiki/Q5419530) |
| 래퍼 곡선 | Laffer curve | 07, 11f | H21 | [Laffer curve](https://zbw.eu/stw/descriptor/19400-3) | 같은 개념 | [Q504749](https://www.wikidata.org/wiki/Q504749) |
| 세수 | tax revenue | 07 | H21 | [Tax revenue](https://zbw.eu/stw/descriptor/11635-2) | 같은 개념 | [Q385503](https://www.wikidata.org/wiki/Q385503) |
| 쐐기 | tax wedge | 07 | H21 | [Excess burden](https://zbw.eu/stw/descriptor/11685-1) | 상위어 | [Q5419530](https://www.wikidata.org/wiki/Q5419530) |
| 한계수입 | marginal revenue | 08 | D21 D42 | [Marginal analysis](https://zbw.eu/stw/descriptor/19218-6) | 상위어 | [Q18460372](https://www.wikidata.org/wiki/Q18460372) |
| 시장구조 | market structure | 08 | L11 D40 | [Market structure](https://zbw.eu/stw/descriptor/10905-4) | 같은 개념 | [Q877707](https://www.wikidata.org/wiki/Q877707) |
| 독점적 경쟁 | monopolistic competition | 08 | D43 | [Monopolistic competition](https://zbw.eu/stw/descriptor/19226-0) | 같은 개념 | [Q379579](https://www.wikidata.org/wiki/Q379579) |
| 독점 | monopoly | 08, 11f | D42 L12 | [Monopoly](https://zbw.eu/stw/descriptor/10205-4) | 같은 개념 | [Q43637](https://www.wikidata.org/wiki/Q43637) |
| 과점과 용의자의 딜레마 | oligopoly and prisoners' dilemma | 08, 11f | D43 L13 | [Oligopoly](https://zbw.eu/stw/descriptor/10209-3) | 같은 개념 | [Q103639](https://www.wikidata.org/wiki/Q103639) |
| 완전경쟁시장 | perfect competition | 08, 11f | D41 | [Perfect competition](https://zbw.eu/stw/descriptor/10227-1) | 같은 개념 | [Q183384](https://www.wikidata.org/wiki/Q183384) |
| 용의자의 딜레마 | prisoners' dilemma | 08 | C72 | [Game theory](https://zbw.eu/stw/descriptor/15458-6) | 상위어 | [Q44455](https://www.wikidata.org/wiki/Q44455) |
| 담합 | collusion, cartel | 08 | L41 L13 | [Cartel](https://zbw.eu/stw/descriptor/10923-2) | 같은 개념 | [Q179216](https://www.wikidata.org/wiki/Q179216) |
| 우월전략 | dominant strategy | 08 | C72 | [Game theory](https://zbw.eu/stw/descriptor/15458-6) | 상위어 | [Q44455](https://www.wikidata.org/wiki/Q44455) |
| 자연독점 | natural monopoly | 08 | L43 | [Natural monopoly](https://zbw.eu/stw/descriptor/10208-5) | 같은 개념 | [Q648510](https://www.wikidata.org/wiki/Q648510) |
| 가격수용자 | price taker | 08 | D41 | [Perfect competition](https://zbw.eu/stw/descriptor/10227-1) | 상위어 | [Q183384](https://www.wikidata.org/wiki/Q183384) |
| 코즈의 정리 | Coase theorem | 09 | D62 | [Coase theorem](https://zbw.eu/stw/descriptor/10091-0) | 같은 개념 | [Q1050037](https://www.wikidata.org/wiki/Q1050037) |
| 외부효과 | externality | 09, 11f | D62 H23 | [Externalities](https://zbw.eu/stw/descriptor/10092-5) | 같은 개념 | [Q275372](https://www.wikidata.org/wiki/Q275372) |
| 무임승차 | free riding | 09 | H41 | [Free rider problem](https://zbw.eu/stw/descriptor/11723-5) | 같은 개념 | [Q499215](https://www.wikidata.org/wiki/Q499215) |
| 소득분배와 지니계수 | income distribution and Gini coefficient | 09, 11f | D31 D63 | [Gini coefficient](https://zbw.eu/stw/descriptor/11738-6) | 같은 개념 | [Q162455](https://www.wikidata.org/wiki/Q162455) |
| 로렌츠 곡선 | Lorenz curve | 09 | D31 | [Lorenz curve](https://zbw.eu/stw/descriptor/11742-1) | 같은 개념 | [Q430378](https://www.wikidata.org/wiki/Q430378) |
| 피구세 | Pigouvian tax | 09 | H23 | [Pigouvian tax](https://zbw.eu/stw/descriptor/29667-6) | 같은 개념 | [Q931921](https://www.wikidata.org/wiki/Q931921) |
| 공공재 | public good | 09, 11f | H41 | [Public goods](https://zbw.eu/stw/descriptor/11718-5) | 같은 개념 | [Q272458](https://www.wikidata.org/wiki/Q272458) |
| 10분위분배율 | decile distribution ratio | 09 | D31 | [Income distribution](https://zbw.eu/stw/descriptor/11735-5) | 상위어 | [Q3915542](https://www.wikidata.org/wiki/Q3915542) |
| 외부불경제 | negative externality | 09 | D62 | [Externalities](https://zbw.eu/stw/descriptor/10092-5) | 상위어 | [Q275372](https://www.wikidata.org/wiki/Q275372) |
| 비배제성 | non-excludability | 09 | H41 | [Public goods](https://zbw.eu/stw/descriptor/11718-5) | 상위어 | [Q272458](https://www.wikidata.org/wiki/Q272458) |
| 비경합성 | non-rivalry | 09 | H41 | [Public goods](https://zbw.eu/stw/descriptor/11718-5) | 상위어 | [Q272458](https://www.wikidata.org/wiki/Q272458) |
| 외부경제 | positive externality | 09 | D62 | [Externalities](https://zbw.eu/stw/descriptor/10092-5) | 상위어 | [Q275372](https://www.wikidata.org/wiki/Q275372) |
| 경기변동 | business cycle | 10 | E32 | [Business cycle](https://zbw.eu/stw/descriptor/10338-6) | 같은 개념 | [Q192311](https://www.wikidata.org/wiki/Q192311) |
| GDP와 실질 GDP | GDP and real GDP | 10, 11f | E01 | [Gross domestic product](https://zbw.eu/stw/descriptor/19231-0) | 같은 개념 | [Q12638](https://www.wikidata.org/wiki/Q12638) |
| 인플레이션 | inflation | 10 | E31 | [Inflation](https://zbw.eu/stw/descriptor/11506-6) | 같은 개념 | [Q35865](https://www.wikidata.org/wiki/Q35865) |
| 인플레이션과 필립스 곡선 | inflation and the Phillips curve | 10, 11f | E31 E24 | [Phillips curve](https://zbw.eu/stw/descriptor/10255-3) | 같은 개념 | [Q220841](https://www.wikidata.org/wiki/Q220841) |
| 실망실업자 | discouraged worker | 10 | J64 | [Labour force](https://zbw.eu/stw/descriptor/11271-0) | 상위어 | [Q837543](https://www.wikidata.org/wiki/Q837543) |
| 고용률 | employment rate | 10 | J21 | [Employment](https://zbw.eu/stw/descriptor/11272-5) | 같은 개념 | [Q656365](https://www.wikidata.org/wiki/Q656365) |
| GDP 디플레이터 | GDP deflator | 10 | E01 E31 | [Price index](https://zbw.eu/stw/descriptor/15093-6) | 상위어 | [Q631360](https://www.wikidata.org/wiki/Q631360) |
| GNP | gross national product | 10 | E01 | [National income](https://zbw.eu/stw/descriptor/10265-0) | 같은 개념 | [Q1057397](https://www.wikidata.org/wiki/Q1057397) |
| 경제활동인구 | labor force | 10 | J21 | [Labour force](https://zbw.eu/stw/descriptor/11271-0) | 같은 개념 | [Q837543](https://www.wikidata.org/wiki/Q837543) |
| 명목 GDP | nominal GDP | 10 | E01 | [Gross domestic product](https://zbw.eu/stw/descriptor/19231-0) | 상위어 | [Q12638](https://www.wikidata.org/wiki/Q12638) |
| 실질 GDP | real GDP | 10 | E01 | [Gross domestic product](https://zbw.eu/stw/descriptor/19231-0) | 상위어 | [Q12638](https://www.wikidata.org/wiki/Q12638) |
| 스태그플레이션 | stagflation | 10 | E31 E32 | [Stagflation](https://zbw.eu/stw/descriptor/10412-6) | 같은 개념 | [Q185245](https://www.wikidata.org/wiki/Q185245) |
| 실업률과 고용지표 | unemployment rate and employment indicators | 10, 11f | E24 J64 | [Labour statistics](https://zbw.eu/stw/descriptor/11264-4) | 같은 개념 | [Q1787954](https://www.wikidata.org/wiki/Q1787954) |
| 총수요와 총공급 | aggregate demand and supply | 11, 11f | E32 E63 | [Aggregate demand](https://zbw.eu/stw/descriptor/10237-5) | 같은 개념 | [Q1801078](https://www.wikidata.org/wiki/Q1801078) |
| 구축효과 | crowding-out effect | 11 | E62 | [Crowding out](https://zbw.eu/stw/descriptor/11734-0) | 같은 개념 | [Q1071788](https://www.wikidata.org/wiki/Q1071788) |
| 재정정책 | fiscal policy | 11, 11f | E62 | [Fiscal policy](https://zbw.eu/stw/descriptor/11728-2) | 같은 개념 | [Q11821824](https://www.wikidata.org/wiki/Q11821824) |
| 통화정책과 정책조합 | monetary policy and policy mix | 11, 11f | E52 E63 | [Monetary policy](https://zbw.eu/stw/descriptor/10382-3) | 같은 개념 | [Q178476](https://www.wikidata.org/wiki/Q178476) |
| 승수효과 | multiplier effect | 11 | E12 E62 | [Multiplier](https://zbw.eu/stw/descriptor/10251-4) | 같은 개념 | — |
| 정책조합 | policy mix | 11 | E63 | [Policy mix](https://zbw.eu/stw/descriptor/10395-1) | 같은 개념 | [Q1751420](https://www.wikidata.org/wiki/Q1751420) |
| 총공급 | aggregate supply | 11 | E23 | [Aggregate supply](https://zbw.eu/stw/descriptor/10241-0) | 같은 개념 | [Q2474789](https://www.wikidata.org/wiki/Q2474789) |
| GDP 갭 | output gap | 11 | E32 | [Potential output](https://zbw.eu/stw/descriptor/10239-1) | 같은 개념 | [Q1452339](https://www.wikidata.org/wiki/Q1452339) |
| 기준금리 | policy rate | 11 | E52 E58 | [Monetary policy](https://zbw.eu/stw/descriptor/10382-3) | 상위어 | [Q178476](https://www.wikidata.org/wiki/Q178476) |

## 쓴 JEL 코드

| 코드 | 제목 |
|---|---|
| A10 | General Economics: General |
| A11 | Role of Economics • Role of Economists • Market for Economists |
| B41 | Economic Methodology |
| C72 | Noncooperative Games |
| D01 | Microeconomic Behavior: Underlying Principles |
| D11 | Consumer Economics: Theory |
| D12 | Consumer Economics: Empirical Analysis |
| D21 | Firm Behavior: Theory |
| D24 | Production • Cost • Capital • Capital, Total Factor, and Multifactor Productivity • Capacity |
| D31 | Personal Income, Wealth, and Their Distributions |
| D40 | Market Structure, Pricing, and Design: General |
| D41 | Perfect Competition |
| D42 | Monopoly |
| D43 | Oligopoly and Other Forms of Market Imperfection |
| D45 | Rationing • Licensing |
| D61 | Allocative Efficiency • Cost–Benefit Analysis |
| D62 | Externalities |
| D63 | Equity, Justice, Inequality, and Other Normative Criteria and Measurement |
| E01 | Measurement and Data on National Income and Product Accounts and Wealth • Environmental Accounts |
| E12 | Keynes • Keynesian • Post-Keynesian • Modern Monetary Theory |
| E21 | Consumption • Saving • Wealth |
| E23 | Production |
| E24 | Employment • Unemployment • Wages • Intergenerational Income Distribution • Aggregate Human Capital • Aggregate Labor Productivity |
| E31 | Price Level • Inflation • Deflation |
| E32 | Business Fluctuations • Cycles |
| E52 | Monetary Policy |
| E58 | Central Banks and Their Policies |
| E62 | Fiscal Policy • Modern Monetary Theory |
| E63 | Comparative or Joint Analysis of Fiscal and Monetary Policy • Stabilization • Treasury Policy |
| H21 | Efficiency • Optimal Taxation |
| H22 | Incidence |
| H23 | Externalities • Redistributive Effects • Environmental Taxes and Subsidies |
| H41 | Public Goods |
| H55 | Social Security and Public Pensions |
| J21 | Labor Force and Employment, Size, and Structure |
| J38 | Public Policy |
| J64 | Unemployment: Models, Duration, Incidence, and Job Search |
| L11 | Production, Pricing, and Market Structure • Size Distribution of Firms |
| L12 | Monopoly • Monopolization Strategies |
| L13 | Oligopoly and Other Imperfect Markets |
| L41 | Monopolization • Horizontal Anticompetitive Practices |
| L43 | Legal Monopolies and Regulation or Deregulation |
| O40 | Economic Growth and Aggregate Productivity: General |
| O47 | Empirical Studies of Economic Growth • Aggregate Productivity • Cross-Country Output Convergence |
