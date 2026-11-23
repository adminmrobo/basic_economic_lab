# -*- coding: utf-8 -*-
"""경제학 표준 색인어 대응표 (2026-11-24 확인)
- STW: ZBW STW Thesaurus for Economics. ID·라벨은 zbw.eu econ-ws suggest 조회 결과, 관계(rel)는 closeMatch(같은 개념)·broadMatch(STW 쪽이 더 넓음)·relatedMatch(관련).
- Wikidata: 각 STW 항목 페이지(zbw.eu/stw/descriptor/<ID>)에 적힌 대응만 옮겼다(직접 추정한 값 없음). STW 쪽에 대응이 없으면 비운다.
- JEL: 미국경제학회 JEL 분류(aeaweb.org/econlit/jelCodes.php)에서 코드·제목을 확인한 뒤 개념별로 배정(dct:subject).
키: lab:concept/<키> 또는 lab:term/<키> (term/ 접두어)."""
JEL_TITLE = {
 "A10": "General Economics: General",
 "A11": "Role of Economics • Role of Economists • Market for Economists",
 "B41": "Economic Methodology",
 "C72": "Noncooperative Games",
 "D01": "Microeconomic Behavior: Underlying Principles",
 "D11": "Consumer Economics: Theory",
 "D12": "Consumer Economics: Empirical Analysis",
 "D21": "Firm Behavior: Theory",
 "D24": "Production • Cost • Capital • Capital, Total Factor, and Multifactor Productivity • Capacity",
 "D31": "Personal Income, Wealth, and Their Distributions",
 "D40": "Market Structure, Pricing, and Design: General",
 "D41": "Perfect Competition",
 "D42": "Monopoly",
 "D43": "Oligopoly and Other Forms of Market Imperfection",
 "D45": "Rationing • Licensing",
 "D61": "Allocative Efficiency • Cost–Benefit Analysis",
 "D62": "Externalities",
 "D63": "Equity, Justice, Inequality, and Other Normative Criteria and Measurement",
 "E01": "Measurement and Data on National Income and Product Accounts and Wealth • Environmental Accounts",
 "E12": "Keynes • Keynesian • Post-Keynesian • Modern Monetary Theory",
 "E21": "Consumption • Saving • Wealth",
 "E23": "Production",
 "E24": "Employment • Unemployment • Wages • Intergenerational Income Distribution • Aggregate Human Capital • Aggregate Labor Productivity",
 "E31": "Price Level • Inflation • Deflation",
 "E32": "Business Fluctuations • Cycles",
 "E52": "Monetary Policy",
 "E58": "Central Banks and Their Policies",
 "E62": "Fiscal Policy • Modern Monetary Theory",
 "E63": "Comparative or Joint Analysis of Fiscal and Monetary Policy • Stabilization • Treasury Policy",
 "H21": "Efficiency • Optimal Taxation",
 "H22": "Incidence",
 "H23": "Externalities • Redistributive Effects • Environmental Taxes and Subsidies",
 "H41": "Public Goods",
 "H55": "Social Security and Public Pensions",
 "J21": "Labor Force and Employment, Size, and Structure",
 "J38": "Public Policy",
 "J64": "Unemployment: Models, Duration, Incidence, and Job Search",
 "L11": "Production, Pricing, and Market Structure • Size Distribution of Firms",
 "L12": "Monopoly • Monopolization Strategies",
 "L13": "Oligopoly and Other Imperfect Markets",
 "L41": "Monopolization • Horizontal Anticompetitive Practices",
 "L43": "Legal Monopolies and Regulation or Deregulation",
 "O40": "Economic Growth and Aggregate Productivity: General",
 "O47": "Empirical Studies of Economic Growth • Aggregate Productivity • Cross-Country Output Convergence"
}
VOCAB = {
 "opportunity-cost": {
  "stw": "10052-3",
  "stw_label": "Opportunity cost",
  "rel": "closeMatch",
  "wd": "Q185715",
  "jel": [
   "D01"
  ]
 },
 "sunk-cost": {
  "stw": "19432-4",
  "stw_label": "Sunk costs",
  "rel": "closeMatch",
  "wd": "Q958242",
  "jel": [
   "D01"
  ]
 },
 "incentive": {
  "stw": "19533-5",
  "stw_label": "Incentives",
  "rel": "closeMatch",
  "wd": "Q1414816",
  "jel": [
   "D01"
  ]
 },
 "marginal-cost": {
  "stw": "20881-0",
  "stw_label": "Marginal costs",
  "rel": "closeMatch",
  "wd": "Q382444",
  "jel": [
   "D01",
   "D24"
  ]
 },
 "consumer-surplus": {
  "stw": "10180-1",
  "stw_label": "Consumer surplus",
  "rel": "closeMatch",
  "wd": "Q361800",
  "jel": [
   "D61"
  ]
 },
 "externality": {
  "stw": "10092-5",
  "stw_label": "Externalities",
  "rel": "closeMatch",
  "wd": "Q275372",
  "jel": [
   "D62",
   "H23"
  ]
 },
 "monopoly": {
  "stw": "10205-4",
  "stw_label": "Monopoly",
  "rel": "closeMatch",
  "wd": "Q43637",
  "jel": [
   "D42",
   "L12"
  ]
 },
 "price-elasticity": {
  "stw": "10055-4",
  "stw_label": "Price elasticity",
  "rel": "closeMatch",
  "wd": "Q3194154",
  "jel": [
   "D11",
   "D12"
  ]
 },
 "deadweight-loss": {
  "stw": "11685-1",
  "stw_label": "Excess burden",
  "rel": "closeMatch",
  "wd": "Q5419530",
  "jel": [
   "H21"
  ]
 },
 "oligopoly": {
  "stw": "10209-3",
  "stw_label": "Oligopoly",
  "rel": "closeMatch",
  "wd": "Q103639",
  "jel": [
   "D43",
   "L13"
  ]
 },
 "public-good": {
  "stw": "11718-5",
  "stw_label": "Public goods",
  "rel": "closeMatch",
  "wd": "Q272458",
  "jel": [
   "H41"
  ]
 },
 "pigouvian-tax": {
  "stw": "29667-6",
  "stw_label": "Pigouvian tax",
  "rel": "closeMatch",
  "wd": "Q931921",
  "jel": [
   "H23"
  ]
 },
 "gini": {
  "stw": "11738-6",
  "stw_label": "Gini coefficient",
  "rel": "closeMatch",
  "wd": "Q162455",
  "jel": [
   "D31",
   "D63"
  ]
 },
 "lorenz-curve": {
  "stw": "11742-1",
  "stw_label": "Lorenz curve",
  "rel": "closeMatch",
  "wd": "Q430378",
  "jel": [
   "D31"
  ]
 },
 "market-failure": {
  "stw": "11054-1",
  "stw_label": "Market failure",
  "rel": "closeMatch",
  "wd": "Q622657",
  "jel": [
   "D61",
   "D62"
  ]
 },
 "market-equilibrium": {
  "stw": "30553-4",
  "stw_label": "Market equilibrium",
  "rel": "closeMatch",
  "wd": "",
  "jel": [
   "D40"
  ]
 },
 "price-ceiling": {
  "stw": "10978-5",
  "stw_label": "Price regulation",
  "rel": "closeMatch",
  "wd": "Q9305568",
  "jel": [
   "D45"
  ]
 },
 "free-riding": {
  "stw": "11723-5",
  "stw_label": "Free rider problem",
  "rel": "closeMatch",
  "wd": "Q499215",
  "jel": [
   "H41"
  ]
 },
 "coase-theorem": {
  "stw": "10091-0",
  "stw_label": "Coase theorem",
  "rel": "closeMatch",
  "wd": "Q1050037",
  "jel": [
   "D62"
  ]
 },
 "term/minimum-wage": {
  "stw": "11328-4",
  "stw_label": "Minimum wage",
  "rel": "closeMatch",
  "wd": "Q186228",
  "jel": [
   "J38"
  ]
 },
 "tax-incidence": {
  "stw": "11692-4",
  "stw_label": "Tax incidence",
  "rel": "closeMatch",
  "wd": "Q2165871",
  "jel": [
   "H22"
  ]
 },
 "laffer-curve": {
  "stw": "19400-3",
  "stw_label": "Laffer curve",
  "rel": "closeMatch",
  "wd": "Q504749",
  "jel": [
   "H21"
  ]
 },
 "perfect-competition": {
  "stw": "10227-1",
  "stw_label": "Perfect competition",
  "rel": "closeMatch",
  "wd": "Q183384",
  "jel": [
   "D41"
  ]
 },
 "monopolistic-competition": {
  "stw": "19226-0",
  "stw_label": "Monopolistic competition",
  "rel": "closeMatch",
  "wd": "Q379579",
  "jel": [
   "D43"
  ]
 },
 "market-structure": {
  "stw": "10905-4",
  "stw_label": "Market structure",
  "rel": "closeMatch",
  "wd": "Q877707",
  "jel": [
   "L11",
   "D40"
  ]
 },
 "fiscal-policy": {
  "stw": "11728-2",
  "stw_label": "Fiscal policy",
  "rel": "closeMatch",
  "wd": "Q11821824",
  "jel": [
   "E62"
  ]
 },
 "monetary-policy": {
  "stw": "10382-3",
  "stw_label": "Monetary policy",
  "rel": "closeMatch",
  "wd": "Q178476",
  "jel": [
   "E52",
   "E63"
  ]
 },
 "prisoners-dilemma": {
  "stw": "15458-6",
  "stw_label": "Game theory",
  "rel": "broadMatch",
  "wd": "Q44455",
  "jel": [
   "C72"
  ]
 },
 "policy-mix": {
  "stw": "10395-1",
  "stw_label": "Policy mix",
  "rel": "closeMatch",
  "wd": "Q1751420",
  "jel": [
   "E63"
  ]
 },
 "crowding-out": {
  "stw": "11734-0",
  "stw_label": "Crowding out",
  "rel": "closeMatch",
  "wd": "Q1071788",
  "jel": [
   "E62"
  ]
 },
 "multiplier": {
  "stw": "10251-4",
  "stw_label": "Multiplier",
  "rel": "closeMatch",
  "wd": "",
  "jel": [
   "E12",
   "E62"
  ]
 },
 "aggregate-demand": {
  "stw": "10237-5",
  "stw_label": "Aggregate demand",
  "rel": "closeMatch",
  "wd": "Q1801078",
  "jel": [
   "E32",
   "E63"
  ]
 },
 "phillips-curve": {
  "stw": "10255-3",
  "stw_label": "Phillips curve",
  "rel": "closeMatch",
  "wd": "Q220841",
  "jel": [
   "E31",
   "E24"
  ]
 },
 "term/aggregate-supply": {
  "stw": "10241-0",
  "stw_label": "Aggregate supply",
  "rel": "closeMatch",
  "wd": "Q2474789",
  "jel": [
   "E23"
  ]
 },
 "business-cycle": {
  "stw": "10338-6",
  "stw_label": "Business cycle",
  "rel": "closeMatch",
  "wd": "Q192311",
  "jel": [
   "E32"
  ]
 },
 "inflation": {
  "stw": "11506-6",
  "stw_label": "Inflation",
  "rel": "closeMatch",
  "wd": "Q35865",
  "jel": [
   "E31"
  ]
 },
 "term/stagflation": {
  "stw": "10412-6",
  "stw_label": "Stagflation",
  "rel": "closeMatch",
  "wd": "Q185245",
  "jel": [
   "E31",
   "E32"
  ]
 },
 "gdp": {
  "stw": "19231-0",
  "stw_label": "Gross domestic product",
  "rel": "closeMatch",
  "wd": "Q12638",
  "jel": [
   "E01"
  ]
 },
 "unemployment-rate": {
  "stw": "11264-4",
  "stw_label": "Labour statistics",
  "rel": "closeMatch",
  "wd": "Q1787954",
  "jel": [
   "E24",
   "J64"
  ]
 },
 "economic-growth": {
  "stw": "10414-2",
  "stw_label": "Economic growth",
  "rel": "closeMatch",
  "wd": "Q189833",
  "jel": [
   "O40",
   "O47"
  ]
 },
 "ppf": {
  "stw": "10328-2",
  "stw_label": "Technical efficiency",
  "rel": "closeMatch",
  "wd": "Q376791",
  "jel": [
   "D24"
  ]
 },
 "microeconomics": {
  "stw": "10144-5",
  "stw_label": "Microeconomics",
  "rel": "closeMatch",
  "wd": "Q39072",
  "jel": [
   "A10"
  ]
 },
 "macroeconomics": {
  "stw": "10249-5",
  "stw_label": "Macroeconomics",
  "rel": "closeMatch",
  "wd": "Q39680",
  "jel": [
   "A10"
  ]
 },
 "economic-model": {
  "stw": "10065-1",
  "stw_label": "Economic model",
  "rel": "closeMatch",
  "wd": "Q2180497",
  "jel": [
   "B41"
  ]
 },
 "consumption-function": {
  "stw": "10181-6",
  "stw_label": "Consumption theory",
  "rel": "broadMatch",
  "wd": "Q1002494",
  "jel": [
   "E21"
  ]
 },
 "demand": {
  "stw": "10013-6",
  "stw_label": "Demand",
  "rel": "closeMatch",
  "wd": "Q4402708",
  "jel": [
   "D11"
  ]
 },
 "supply": {
  "stw": "10000-1",
  "stw_label": "Supply",
  "rel": "closeMatch",
  "wd": "Q542869",
  "jel": [
   "D21"
  ]
 },
 "efficiency": {
  "stw": "11039-4",
  "stw_label": "Efficiency",
  "rel": "closeMatch",
  "wd": "Q1034411",
  "jel": [
   "D61"
  ]
 },
 "total-surplus": {
  "stw": "10113-2",
  "stw_label": "Welfare economics",
  "rel": "broadMatch",
  "wd": "Q851147",
  "jel": [
   "D61"
  ]
 },
 "income-cross-elasticity": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "closeMatch",
  "wd": "Q223639",
  "jel": [
   "D11",
   "D12"
  ]
 },
 "elasticity-dwl": {
  "stw": "11685-1",
  "stw_label": "Excess burden",
  "rel": "closeMatch",
  "wd": "Q5419530",
  "jel": [
   "H21"
  ]
 },
 "income-elasticity": {
  "stw": "10171-2",
  "stw_label": "Income elasticity of demand",
  "rel": "closeMatch",
  "wd": "Q734113",
  "jel": [
   "D12"
  ]
 },
 "willingness-to-pay": {
  "stw": "19210-1",
  "stw_label": "Willingness to pay",
  "rel": "closeMatch",
  "wd": "Q140813",
  "jel": [
   "D11"
  ]
 },
 "normative-economics": {
  "stw": "19989-4",
  "stw_label": "Normative economics",
  "rel": "closeMatch",
  "wd": "Q26086",
  "jel": [
   "B41",
   "D63"
  ]
 },
 "marginal-thinking": {
  "stw": "19218-6",
  "stw_label": "Marginal analysis",
  "rel": "closeMatch",
  "wd": "Q18460372",
  "jel": [
   "D01"
  ]
 },
 "positive-normative": {
  "stw": "19989-4",
  "stw_label": "Normative economics",
  "rel": "closeMatch",
  "wd": "Q26086",
  "jel": [
   "B41"
  ]
 },
 "positive-economics": {
  "stw": "20022-6",
  "stw_label": "Positive economics",
  "rel": "closeMatch",
  "wd": "Q26110",
  "jel": [
   "B41"
  ]
 },
 "total-revenue": {
  "stw": "12311-2",
  "stw_label": "Revenue",
  "rel": "closeMatch",
  "wd": "Q350205",
  "jel": [
   "D21"
  ]
 },
 "elasticity-revenue": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11",
   "D21"
  ]
 },
 "supply-elasticity": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D21"
  ]
 },
 "cross-elasticity": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11"
  ]
 },
 "price-floor": {
  "stw": "10978-5",
  "stw_label": "Price regulation",
  "rel": "broadMatch",
  "wd": "Q9305568",
  "jel": [
   "J38"
  ]
 },
 "equity": {
  "stw": "10110-1",
  "stw_label": "Distributive justice",
  "rel": "closeMatch",
  "wd": "Q552284",
  "jel": [
   "D63"
  ]
 },
 "marginal-benefit": {
  "stw": "19218-6",
  "stw_label": "Marginal analysis",
  "rel": "broadMatch",
  "wd": "Q18460372",
  "jel": [
   "D01"
  ]
 },
 "marginal-revenue": {
  "stw": "19218-6",
  "stw_label": "Marginal analysis",
  "rel": "broadMatch",
  "wd": "Q18460372",
  "jel": [
   "D21",
   "D42"
  ]
 },
 "term/substitutes": {
  "stw": "18129-3",
  "stw_label": "Substitute goods",
  "rel": "closeMatch",
  "wd": "Q312588",
  "jel": [
   "D11"
  ]
 },
 "term/complements": {
  "stw": "29965-5",
  "stw_label": "Complementary goods",
  "rel": "closeMatch",
  "wd": "",
  "jel": [
   "D11"
  ]
 },
 "term/inferior-good": {
  "stw": "10178-2",
  "stw_label": "Inferior goods",
  "rel": "closeMatch",
  "wd": "Q588065",
  "jel": [
   "D11"
  ]
 },
 "term/black-market": {
  "stw": "10845-3",
  "stw_label": "Illicit trade",
  "rel": "closeMatch",
  "wd": "Q57262007",
  "jel": [
   "D45"
  ]
 },
 "term/rationing": {
  "stw": "11034-0",
  "stw_label": "Rationing",
  "rel": "closeMatch",
  "wd": "Q843478",
  "jel": [
   "D45"
  ]
 },
 "term/labor-force": {
  "stw": "11271-0",
  "stw_label": "Labour force",
  "rel": "closeMatch",
  "wd": "Q837543",
  "jel": [
   "J21"
  ]
 },
 "term/employment-rate": {
  "stw": "11272-5",
  "stw_label": "Employment",
  "rel": "closeMatch",
  "wd": "Q656365",
  "jel": [
   "J21"
  ]
 },
 "term/gnp": {
  "stw": "10265-0",
  "stw_label": "National income",
  "rel": "closeMatch",
  "wd": "Q1057397",
  "jel": [
   "E01"
  ]
 },
 "term/output-gap": {
  "stw": "10239-1",
  "stw_label": "Potential output",
  "rel": "closeMatch",
  "wd": "Q1452339",
  "jel": [
   "E32"
  ]
 },
 "term/natural-monopoly": {
  "stw": "10208-5",
  "stw_label": "Natural monopoly",
  "rel": "closeMatch",
  "wd": "Q648510",
  "jel": [
   "L43"
  ]
 },
 "term/price-discrimination": {
  "stw": "10215-1",
  "stw_label": "Price discrimination",
  "rel": "closeMatch",
  "wd": "Q835678",
  "jel": [
   "D42"
  ]
 },
 "term/collusion": {
  "stw": "10923-2",
  "stw_label": "Cartel",
  "rel": "closeMatch",
  "wd": "Q179216",
  "jel": [
   "L41",
   "L13"
  ]
 },
 "term/tax-revenue": {
  "stw": "11635-2",
  "stw_label": "Tax revenue",
  "rel": "closeMatch",
  "wd": "Q385503",
  "jel": [
   "H21"
  ]
 },
 "term/dominant-strategy": {
  "stw": "15458-6",
  "stw_label": "Game theory",
  "rel": "broadMatch",
  "wd": "Q44455",
  "jel": [
   "C72"
  ]
 },
 "term/non-rivalry": {
  "stw": "11718-5",
  "stw_label": "Public goods",
  "rel": "broadMatch",
  "wd": "Q272458",
  "jel": [
   "H41"
  ]
 },
 "term/non-excludability": {
  "stw": "11718-5",
  "stw_label": "Public goods",
  "rel": "broadMatch",
  "wd": "Q272458",
  "jel": [
   "H41"
  ]
 },
 "term/positive-externality": {
  "stw": "10092-5",
  "stw_label": "Externalities",
  "rel": "broadMatch",
  "wd": "Q275372",
  "jel": [
   "D62"
  ]
 },
 "term/negative-externality": {
  "stw": "10092-5",
  "stw_label": "Externalities",
  "rel": "broadMatch",
  "wd": "Q275372",
  "jel": [
   "D62"
  ]
 },
 "term/real-gdp": {
  "stw": "19231-0",
  "stw_label": "Gross domestic product",
  "rel": "broadMatch",
  "wd": "Q12638",
  "jel": [
   "E01"
  ]
 },
 "term/nominal-gdp": {
  "stw": "19231-0",
  "stw_label": "Gross domestic product",
  "rel": "broadMatch",
  "wd": "Q12638",
  "jel": [
   "E01"
  ]
 },
 "term/quantity-demanded": {
  "stw": "10013-6",
  "stw_label": "Demand",
  "rel": "broadMatch",
  "wd": "Q4402708",
  "jel": [
   "D11"
  ]
 },
 "term/quantity-supplied": {
  "stw": "10000-1",
  "stw_label": "Supply",
  "rel": "broadMatch",
  "wd": "Q542869",
  "jel": [
   "D21"
  ]
 },
 "term/statutory-incidence": {
  "stw": "11692-4",
  "stw_label": "Tax incidence",
  "rel": "broadMatch",
  "wd": "Q2165871",
  "jel": [
   "H22"
  ]
 },
 "term/economic-incidence": {
  "stw": "11692-4",
  "stw_label": "Tax incidence",
  "rel": "broadMatch",
  "wd": "Q2165871",
  "jel": [
   "H22"
  ]
 },
 "term/increasing-opportunity-cost": {
  "stw": "10052-3",
  "stw_label": "Opportunity cost",
  "rel": "broadMatch",
  "wd": "Q185715",
  "jel": [
   "D24"
  ]
 },
 "term/implicit-cost": {
  "stw": "10052-3",
  "stw_label": "Opportunity cost",
  "rel": "broadMatch",
  "wd": "Q185715",
  "jel": [
   "D24"
  ]
 },
 "term/arc-elasticity": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11"
  ]
 },
 "term/elastic": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11"
  ]
 },
 "term/inelastic": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11"
  ]
 },
 "term/unit-elastic": {
  "stw": "10036-1",
  "stw_label": "Elasticity",
  "rel": "broadMatch",
  "wd": "Q223639",
  "jel": [
   "D11"
  ]
 },
 "term/tax-wedge": {
  "stw": "11685-1",
  "stw_label": "Excess burden",
  "rel": "broadMatch",
  "wd": "Q5419530",
  "jel": [
   "H21"
  ]
 },
 "term/discouraged-worker": {
  "stw": "11271-0",
  "stw_label": "Labour force",
  "rel": "broadMatch",
  "wd": "Q837543",
  "jel": [
   "J64"
  ]
 },
 "term/decile-ratio": {
  "stw": "11735-5",
  "stw_label": "Income distribution",
  "rel": "broadMatch",
  "wd": "Q3915542",
  "jel": [
   "D31"
  ]
 },
 "term/excess-demand": {
  "stw": "30553-4",
  "stw_label": "Market equilibrium",
  "rel": "broadMatch",
  "wd": "",
  "jel": [
   "D40"
  ]
 },
 "term/excess-supply": {
  "stw": "30553-4",
  "stw_label": "Market equilibrium",
  "rel": "broadMatch",
  "wd": "",
  "jel": [
   "D40"
  ]
 },
 "term/mpc": {
  "stw": "10181-6",
  "stw_label": "Consumption theory",
  "rel": "broadMatch",
  "wd": "Q1002494",
  "jel": [
   "E21"
  ]
 },
 "willingness-to-sell": {
  "stw": "19210-1",
  "stw_label": "Willingness to pay",
  "rel": "relatedMatch",
  "wd": "Q140813",
  "jel": [
   "D21"
  ]
 },
 "producer-surplus": {
  "stw": "10113-2",
  "stw_label": "Welfare economics",
  "rel": "broadMatch",
  "wd": "Q851147",
  "jel": [
   "D61"
  ]
 },
 "term/tax-shifting": {
  "stw": "11692-4",
  "stw_label": "Tax incidence",
  "rel": "closeMatch",
  "wd": "Q2165871",
  "jel": [
   "H22"
  ]
 },
 "term/economic-profit": {
  "stw": "12275-1",
  "stw_label": "Profit",
  "rel": "broadMatch",
  "wd": "Q26911",
  "jel": [
   "D21"
  ]
 },
 "term/policy-rate": {
  "stw": "10382-3",
  "stw_label": "Monetary policy",
  "rel": "broadMatch",
  "wd": "Q178476",
  "jel": [
   "E52",
   "E58"
  ]
 },
 "term/normal-good": {
  "stw": "10171-2",
  "stw_label": "Income elasticity of demand",
  "rel": "relatedMatch",
  "wd": "Q734113",
  "jel": [
   "D11"
  ]
 },
 "term/assumption": {
  "stw": "10065-1",
  "stw_label": "Economic model",
  "rel": "broadMatch",
  "wd": "Q2180497",
  "jel": [
   "B41"
  ]
 },
 "term/price-taker": {
  "stw": "10227-1",
  "stw_label": "Perfect competition",
  "rel": "broadMatch",
  "wd": "Q183384",
  "jel": [
   "D41"
  ]
 },
 "term/explicit-cost": {
  "stw": "10011-3",
  "stw_label": "Costs",
  "rel": "broadMatch",
  "wd": "Q240673",
  "jel": [
   "D24"
  ]
 },
 "term/gdp-deflator": {
  "stw": "15093-6",
  "stw_label": "Price index",
  "rel": "broadMatch",
  "wd": "Q631360",
  "jel": [
   "E01",
   "E31"
  ]
 },
 "term/transfer-income": {
  "stw": "11569-3",
  "stw_label": "Social security benefits",
  "rel": "relatedMatch",
  "wd": "Q59284985",
  "jel": [
   "H55"
  ]
 },
 "scarcity": {
  "jel": [
   "A10",
   "D01"
  ]
 },
 "trade-off": {
  "jel": [
   "D01"
  ]
 },
 "term/economic-good": {
  "jel": [
   "D01"
  ]
 },
 "term/free-good": {
  "jel": [
   "D01"
  ]
 }
}
