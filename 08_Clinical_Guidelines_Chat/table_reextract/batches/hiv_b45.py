exec(open("batches/hiv_common.py").read())
# HIV 2022 part 5, pp.287-289 (Annex 11.16 Alternative ART for paediatric clients on TB treatment). Cell text from the ruled grid,
# structure from the page images.
AN = "Chapter 11: Annexes"
INIT, ONART = "Initiating ARVs while on ATT", "Initiating TB treatment while receiving ART"
SUPER = "If VL >1000 copies/mL:<br/>- Adherence counselling<br/>- Consider alternative formulations of LPV/r including pellets"
ITEMS = [
 T("tbl-11.16-paediatric-art-on-tb-treatment", 287, AN + " > 11.16 Alternative ART for Pediatric Clients on TB Treatment", "Annex 11.16 Alternative ART for Paediatric Clients on TB Treatment", ["0777", "0778", "0779", "0780"],
   [r("Consideration", "Current situation", "Regimen", "Comments")],
   [{"section": "Infants and children <3 years or < 10 kg"},
    [C(INIT, rs=3), C("", rs=3), C("Recommended: ABC+3TC+AZT while on ATT"), C("Avoid in settings of severe immunosuppression, CD4 <15%. Check VL at the end of ATT. Change to LPV/r at TB treatment completion.")],
    r("Alternative 1: ABC(AZT)+3TC+LPV/r. Super boosting with 1:1 ritonavir for the duration of TB treatment", "Check VL at the end of ATT. Change back to LPV/r standard dosing after TB treatment. If VL is undetectable, conduct SUAC and consider genotyping."),
    r("Alternative 2: ABC(AZT)+3TC+NVP for the duration of ATT", "Check VL at the end of ATT"),
    [C(ONART, rs=4), C("Child on standard first-line PI-based regimen (2 NRTIs + LPV/r)", rs=3), C("Recommended: Substitute to ABC+3TC+AZT while on ATT"), C("Check VL at the end of ATT. Change back to LPV/r after TB treatment.")],
    r("Alternative 1: Continue ABC (AZT)+3TC+LPV/r. Super-boosting with 1:1 ritonavir for the duration of TB treatment", "Consider if the client currently tolerates standard dose LPV/r without a problem.<br/>" + SUPER),
    r("Alternative 2: Transition to ABC(AZT)+3TC+NVP", "- Consider if poor tolerability is already limiting the efficacy of the LPV/r-based regimen<br/>- Adherence counselling<br/>- Check VL at the end of ATT or earlier if clinical deterioration<br/>- Continue NNRTI-based regimen if VL is undetectable at the end of ATT"),
    r("Child on standard NNRTI-based regimen (NVP)", "Recommended: Continue ABC(AZT)+3TC+NVP", "Check VL at the end of ATT and continue NNRTI based regimen if VL is undetectable"),
    {"section": "Children and adolescents 3 years and older"},
    [C("Initiating ARVs while on TB treatment (ATT)", rs=3), C("> 3 years, <10 kg"), C("Recommended: ABC(AZT)+3TC +EFV"), C("")],
    [C("> 12 years, >40 kg", rs=2), C("Recommended: TDF+3TC+EFV"), C("Check VL at the end of TB treatment. If VL is undetectable, substitute EFV with DTG")],
    r("Alternative: ABC+3TC+AZT while on ATT", "Check VL at the end of ATT. Change back to LPV/r after TB treatment."),
    [C(ONART, rs=10), C("Child on standard first-line PI-based regimen (2 NRTIs + LPV/r)", rs=3), C("Recommended: Substitute with EFV"), C("Check that the child has no history of failure of an NNRTI-based regimen (VL<1000 copies/mL). Check VL at the end of ATT and continue the NNRTI-based regimen if VL is undetectable.")],
    r("Alternative 1: Substitute to ABC+3TC+AZT while on ATT", "Consider if tolerability is leading to poor adherence with LPV/r or if not tolerating 1:1 ritonavir super boosting (see below). Check VL at the end of ATT. Change back to LPV/r after TB treatment."),
    r("Alternative 2: Continue ABC(AZT)+3TC+LPV/r. Super boosting with 1:1 ritonavir for the duration of TB treatment", "Consider if the client currently tolerates standard dose LPV/r without a problem.<br/>" + SUPER),
    [C("Child on standard NNRTI-based regimen (2 NRTIs + EFV or NVP)", rs=3), C("Recommended: Continue the same regimen if the child is receiving EFV"), C("In children with severe immunosuppression consider fast-track evaluation and initiation of second-line therapy while on ATT.")],
    r("Recommended: If the child is receiving NVP, substitute with EFV", "Check VL at the end of ATT and continue the NNRTI-based regimen if VL is undetectable."),
    r("Alternative 1: Substitute to ABC+3TC+AZT while on ATT", "Check VL at the end of ATT and continue the NNRTI-based regimen if VL is undetectable."),
    r("Adolescent on TDF-3TC-DTG", "Recommendation: Substitute DTG to EFV", "Check VL at the end of ATT, if VL < 100 copies, the client can switch back to DTG"),
    [C("Current regimen LPV/r as second-line", rs=2), C("Recommended: Continue ABC(AZT)+3TC+LPV/r. Super boosting with 1:1 ritonavir for the duration of TB treatment"), C("Consider if the client currently tolerates standard dose LPV/r without a problem.<br/>" + SUPER + "<br/>- Consult doctor and Baylor HIV/TB Hotline for 3rd line evaluation (See Annex 11.14)")],
    r("Alternative 1: Substitute to ABC+3TC+AZT while on ATT", "Avoid in settings of severe immunosuppression. Consider if tolerability of LPV/r is leading to poor adherence and will likely be made worse by increasing the ritonavir dose if not tolerating 1:1 dosing. Adherence counselling. Check VL at the end of ATT"),
    r("Current regimen ATV/r as second-line", "Recommended: Substitute and double LPV/r dose for the duration of ATTs", "Change back to ATV/r after TB treatment.<br/>" + SUPER + "<br/>- Consult doctor and Baylor HIV/TB Hotline for 3rd line evaluation")],
   pages=[287, 288, 289],
   source_flags=["Annex 11.16 says 'If VL is undetectable, conduct SUAC and consider genotyping' (Alternative 1, children <3 years); SUAC and genotyping apply to a detectable VL.",
                 "Annex 11.16 tells adolescents on TDF-3TC-DTG starting TB treatment to substitute DTG with EFV (back to DTG if VL <100 copies); Chapter 9, the adult TB/HIV guidance and the 2024 Amendment (9.4) instead give DTG twice daily during rifampicin-based TB treatment and for 2 weeks after.",
                 "Annex 11.16 is built on LPV/r-, NVP- and EFV-based regimens; the 2024 Amendment table for children starting TB treatment while on ART (DTG twice daily; LPV/r to DTG if DTG-naive; DRV/r or ATV/r replaced) supersedes it."]),
]
