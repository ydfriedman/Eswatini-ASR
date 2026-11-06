exec(open("batches/hiv_common.py").read())
# HIV 2022 part 1, pp.48-54 (Chapter 3: HIV testing services). Cell text from the PDF text layer / ruled grid; structure and
# flowchart branches from the page images.
C3 = "Chapter 3: HIV Testing Services"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
ITEMS = [
 D("fig-3.1-hts-guiding-principles", 48, C3 + " > Guiding Principles of HIV Testing Services > Figure 3.1", "Figure 3.1 Summary Guiding Principles for HIV Testing services", [],
   "Four guiding principles for HIV testing services, arranged around 'Upholding the 5C's' at the centre:\n- Promoting Universal Health Coverage for all\n- Promoting client-centered HIV Testing Services\n- Reducing stigma and discrimination\n- Preventing violence\n"
   "HTS is a critical entry point to HIV prevention, care and treatment; all clients who receive HIV testing should be provided with their results and linked to support, prevention and treatment services, ideally with same-day diagnosis and same-day linkage."),
 T("tbl-3.1-five-cs", 49, C3 + " > Guiding Principles of HIV Testing Services > Preventing violence > Table 3.1 Upholding The 5Cs", "Table 3.1 Upholding The 5Cs", ["0100", "0101"],
   [r("Guiding Principles", "Key Points")],
   [r("Informed Consent/Assent", B_("PIHTS: An opt-out approach is used where HTS is offered by a HCW and consent is assumed unless the client explicitly declines the HIV test.",
        "CIHTS: Clients requesting HTS and verbal consent/assent is obtained to conduct the HIV screening tool or test.",
        "Recency HIV Testing: A written consent is required for all clients eligible for HIV recency testing.",
        "HIVST: A verbal consent for HIVST is obtained for individuals 16years and older; a verbal assent by a legal guardian is obtained for a minor eligible for Paediatric Oral Fluid HIVST")),
    r("Confidentiality", B_("Testing results and any discussions between the HTS provider and the client should not be disclosed to anyone without the expressed consent/assent of the person being tested.",
        "Shared confidentiality among HCWs to promote linkages and further client management should be explained to the client.", "Privacy during testing and counselling should be ensured")),
    r("Counselling (pre and post-test)", B_("Accompany testing with appropriate, brief and high-quality pre-test information and post-test counselling.",
        "Messages should be tailored to the client’s needs and focused on encouraging notification/disclosure of HIV status to sexual partners and family members or trusted others, where beneficial.",
        "Post-test counselling should also include messages designed to facilitate linkages to prevention and treatment services following HIV testing.")),
    r("Correct test results", B_("Perform rapid HIV testing according to the relevant national testing algorithm including confirmation of all reactive self-test results.",
        "Adhere to national quality assurance standards to ensure correct and accurate results are given to the client.",
        "Re-test all people with an HIV-positive diagnosis using the full national rapid HIV testing algorithm before ART initiation.")),
    r("Connections and linkages to prevention, care and treatment", B_("Refer and actively link all clients to appropriate HIV prevention, treatment, and other support services, according to their results."))],
   context_before="The 5 Cs are essential guiding principles to ensure a human rights-based approach in HTS: Consent, Confidentiality, Counselling, Correct test results and Connection to HIV prevention, treatment and care.",
   source_flags=["'A verbal assent by a legal guardian' for a minor's paediatric oral-fluid HIVST: a guardian gives consent; assent is the child's agreement."]),
 D("fig-3.2-targeted-testing", 50, C3 + " > 3.2 HIV testing service delivery approaches > 3.2.1 Targeted testing > Figure 3.2", "Figure 3.2 Targeted Testing", ["0103"],
   "Targeted testing selects people by three kinds of characteristics:\n"
   "- Behavioral characteristics: risky behaviours include anal sex, multiple sexual partners, inconsistent or incorrect condom use, and intravenous drug use\n"
   "- Clinical characteristics: clients with active or presumptive TB, STIs, viral hepatitis and other clinical indications or opportunistic infections\n"
   "- Demographic characteristics: discordant couples, prisoners, migrant/mobile populations, male-dominated industries, pregnant and lactating women, children and adolescents\n"
   "Priority groups: men; children and adolescents (ages 0-19) and young women (15-29); key populations. Targeted testing is done through PIHTS and CIHTS at facility and community level."),
 D("fig-3.3-pihts-master-client-flow", 52, C3 + " > 3.2 HIV testing service delivery approaches > Community-based HIV testing services > Figure 3.3", "Figure 3.3 Provider Initiated HIV Testing Master Client Flow", ["0109"],
   "1. Arrival at community/facility service point.\n"
   "2. Covid-19/TB symptom screening.\n"
   "   - Positive: fast track to Covid-19 testing/TB specimen collection and further investigation, then test for HIV.\n"
   "   - Negative: HTS eligibility assessment.\n"
   "       - Not eligible: proceed to other services.\n"
   "       - Eligible: HIV risk assessment.\n"
   "           - At risk: test for HIV.\n"
   "           - No/low risk: proceed to other services.\n"
   "Requirements: Infrastructure - each facility should designate a well ventilated, private space for TB/Covid-19 screening. Human resources - preferably each facility should have designated personnel to conduct the listed services; a trained HTS counsellor, nurse or doctor should carry out the listed services.",
   flags=["The branch from 'HIV risk assessment' to 'Test for HIV' is not labelled in the figure (only 'No/Low risk' is); read here as 'at risk'."]),
 T("tbl-3.2-hivst-approaches", 53, C3 + " > 3.2.2 HIV Self testing > HIV Self-Testing Approaches > Table 3.2 HIV self-testing approaches", "Table 3.2 HIV self-testing approaches", ["0112"],
   [r("Approach", "Description")],
   [r("Assisted self-testing", "Refers to a trained HTS provider giving an individual an in-person demonstration before or during HIVST on how to perform the test and interpret the test result. This approach can be used to support self-testers with disabilities, low literacy levels and individuals who may require or request direct assistance in the form of in-person demonstrations and explanations before, during and/or after testing. Assisted self-testing can be offered to an individual or a group."),
    r("Unassisted self-testing", "This refers to when an individual self-tests for HIV and uses an HIVST kit without the help of a trained HTS provider and usually in the comfort of their own home.")],
   context_before="HIV self-testing does not provide a definitive HIV-positive diagnosis; any positive result must be confirmed by a HCW following national testing algorithms. The age of consent for HIVST in Eswatini is 16 years."),
 D("fig-3.4-hivst-flow", 53, C3 + " > 3.2.2 HIV Self testing > Figure 3.4 HIV self-testing flow chart", "Figure 3.4 HIV self-testing flow chart", ["0114"],
   "Perform an HIV test using HIVST:\n- Reactive: confirmatory test by HCW required and done as per national HIV testing algorithm.\n- Non reactive: emphasis on the relevant HIV prevention services."),
 T("tbl-3.3-hivst-delivery-models", 54, C3 + " > 3.2.2 HIV Self testing > HIVST delivery models > Table 3.3 HIV self-testing service delivery models", "Table 3.3 HIV self-testing service delivery models", ["0116", "0117"],
   [r("Models", "Description")],
   [r("Community-based", "Distribution during campaigns, at events, mobile outreach or home-based (door-to-door) distribution. Integration with existing community-based testing programs can improve efficiency and optimize resources. Community-led models are likely to be successful."),
    r("Facility-based", "Distribution from facilities or other fixed sites for use later or within the facilities. Kits can be given to HIV-positive or HIV-negative clients for secondary distribution."),
    r("Order online and receive via mail", "A range of online platforms such as websites, social media, dating apps, and other digital media can be used. HIV self-testing kits can be provided for free, at a cost or with coupons/vouchers for a reduced cost."),
    r("Secondary distribution", "Includes secondary distribution to partners or peers including distribution by HIV-negative and HIV-positive clients. Index clients can be given HIV self-testing kits by providers of facilities. Index clients can be given HIV self-testing kits by providers of facilities. Index clients can be given (oral-based) HIVST for testing of their biological child(ren) with unknown HIV status and non-biological children with exposure history and unknown status"),
    r("Private pharmacies", "Distribution from pharmacies for clients who may need testing through public-private partnerships and distribution"),
    r("Retail outlets, and vending machines", "Kits are typically provided at a cost to users but the price can be reduced through public-private partnerships and the distribution of coupons or vouchers."),
    r("Faith-best settings", "Distribution from faith-based settings such as churches and mosques."),
    r("Workplace", "Distribution to workers for testing themselves and/or for their partners. Consider sustainable models such as public-private partnerships and/or insurance packages to cover the cost.")],
   source_flags=["'Faith-best settings' (faith-based). The secondary-distribution row repeats one sentence."]),
]
