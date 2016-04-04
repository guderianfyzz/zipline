MULTI_SIGNAL_CSV_DATA = """
symbol,date,signal
ibm,1/1/06,1
ibm,2/1/06,0
ibm,3/1/06,0
ibm,4/1/06,0
ibm,5/1/06,1
ibm,6/1/06,1
ibm,7/1/06,1
ibm,8/1/06,1
ibm,9/1/06,0
ibm,10/1/06,1
ibm,11/1/06,1
ibm,12/1/06,5
ibm,1/1/07,1
ibm,2/1/07,0
ibm,3/1/07,1
ibm,4/1/07,0
ibm,5/1/07,1
dell,1/1/06,1
dell,2/1/06,0
dell,3/1/06,0
dell,4/1/06,0
dell,5/1/06,1
dell,6/1/06,1
dell,7/1/06,1
dell,8/1/06,1
dell,9/1/06,0
dell,10/1/06,1
dell,11/1/06,1
dell,12/1/06,5
dell,1/1/07,1
dell,2/1/07,0
dell,3/1/07,1
dell,4/1/07,0
dell,5/1/07,1
""".strip()

AAPL_CSV_DATA = """
symbol,date,signal
aapl,1/1/06,1
aapl,2/1/06,0
aapl,3/1/06,0
aapl,4/1/06,0
aapl,5/1/06,1
aapl,6/1/06,1
aapl,7/1/06,1
aapl,8/1/06,1
aapl,9/1/06,0
aapl,10/1/06,1
aapl,11/1/06,1
aapl,12/1/06,5
aapl,1/1/07,1
aapl,2/1/07,0
aapl,3/1/07,1
aapl,4/1/07,0
aapl,5/1/07,1
""".strip()

# times are expected in UTC
AAPL_MINUTE_CSV_DATA = """
symbol,date,signal
aapl,1/4/06 5:31AM, 1
aapl,1/4/06 11:30AM, 2
aapl,1/5/06 5:31AM, 1
aapl,1/5/06 11:30AM, 3
aapl,1/9/06 5:31AM, 1
aapl,1/9/06 11:30AM, 4
""".strip()

IBM_CSV_DATA = """
symbol,date,signal
ibm,1/1/06,1
ibm,2/1/06,0
ibm,3/1/06,0
ibm,4/1/06,0
ibm,5/1/06,1
ibm,6/1/06,1
ibm,7/1/06,1
ibm,8/1/06,1
ibm,9/1/06,0
ibm,10/1/06,1
ibm,11/1/06,1
ibm,12/1/06,5
ibm,1/1/07,1
ibm,2/1/07,0
ibm,3/1/07,1
ibm,4/1/07,0
ibm,5/1/07,1
""".strip()

ANNUAL_AAPL_CSV_DATA = """
symbol,date,signal
aapl,1/2/06,1
aapl,1/15/06,1
aapl,3/1/06,1
aapl,3/15/06,1
aapl,6/1/06,1
aapl,6/15/06,1
aapl,9/1/06,1
aapl,9/15/06,1
aapl,12/1/06,1
aapl,12/15/06,1
""".strip()

AAPL_IBM_CSV_DATA = """
symbol,date,signal
aapl,1/1/06,1
aapl,2/1/06,0
aapl,3/1/06,0
aapl,4/1/06,0
aapl,5/1/06,1
aapl,6/1/06,1
aapl,7/1/06,1
aapl,8/1/06,1
aapl,9/1/06,0
aapl,10/1/06,1
aapl,11/1/06,1
aapl,12/1/06,5
aapl,1/1/07,1
aapl,2/1/07,0
aapl,3/1/07,1
aapl,4/1/07,0
aapl,5/1/07,1
ibm,1/1/06,1
ibm,2/1/06,0
ibm,3/1/06,0
ibm,4/1/06,0
ibm,5/1/06,1
ibm,6/1/06,1
ibm,7/1/06,1
ibm,8/1/06,1
ibm,9/1/06,0
ibm,10/1/06,1
ibm,11/1/06,1
ibm,12/1/06,5
ibm,1/1/07,1
ibm,2/1/07,0
ibm,3/1/07,1
ibm,4/1/07,0
ibm,5/1/07,1
""".strip()

CPIAUCSL_DATA = """
Date,Value
2007-12-01,211.445
2007-11-01,210.834
2007-10-01,209.19
2007-09-01,208.547
2007-08-01,207.667
2007-07-01,207.603
2007-06-01,207.234
2007-05-01,206.755
2007-04-01,205.904
2007-03-01,205.288
2007-02-01,204.226
2007-01-01,203.437
2006-12-01,203.1
2006-11-01,202.0
2006-10-01,201.9
2006-09-01,202.8
2006-08-01,203.8
2006-07-01,202.9
2006-06-01,201.8
2006-05-01,201.3
2006-04-01,200.7
2006-03-01,199.7
2006-02-01,199.4
2006-01-01,199.3
""".strip()

PALLADIUM_DATA = """
Date,Hong Kong 8:30,Hong Kong 14:00,London 08:00,New York 9:30,New York 15:00
2007-12-31,367.0,367.0,368.0,368.0,368.0
2007-12-28,366.0,366.0,365.0,368.0,368.0
2007-12-27,367.0,367.0,366.0,363.0,367.0
2007-12-26,,,,365.0,365.0
2007-12-24,351.0,357.0,357.0,357.0,365.0
2007-12-21,356.0,356.0,354.0,357.0,357.0
2007-12-20,357.0,356.0,354.0,356.0,356.0
2007-12-19,359.0,359.0,359.0,356.0,358.0
2007-12-18,357.0,356.0,356.0,359.0,359.0
2007-12-17,353.0,353.0,351.0,354.0,360.0
2007-12-14,347.0,347.0,347.0,347.0,355.0
2007-12-13,349.0,349.0,349.0,349.0,347.0
2007-12-12,348.0,349.0,349.0,351.0,349.0
2007-12-11,346.0,346.0,346.0,348.0,350.0
2007-12-10,346.0,346.0,346.0,348.0,348.0
2007-12-07,348.0,348.0,348.0,346.0,346.0
2007-12-06,350.0,350.0,352.0,348.0,348.0
2007-12-05,350.0,350.0,352.0,351.0,351.0
2007-12-04,349.0,349.0,352.0,351.0,351.0
2007-12-03,350.0,350.0,354.0,350.0,350.0
2007-11-30,345.0,345.0,347.0,353.0,350.0
2007-11-29,348.0,348.0,348.0,347.0,345.0
2007-11-28,350.0,347.0,347.0,348.0,348.0
2007-11-27,356.0,356.0,358.0,354.0,350.0
2007-11-26,357.0,357.0,360.0,360.0,360.0
2007-11-23,353.0,354.0,357.0,355.0,
2007-11-22,359.0,359.0,359.0,358.0,
2007-11-21,364.0,364.0,366.0,365.0,359.0
2007-11-20,360.0,359.0,362.0,364.0,364.0
2007-11-19,366.0,365.0,365.0,365.0,361.0
2007-11-16,368.0,366.0,368.0,369.0,366.0
2007-11-15,373.0,372.0,372.0,368.0,368.0
2007-11-14,372.0,372.0,372.0,373.0,373.0
2007-11-13,365.0,365.0,368.0,372.0,372.0
2007-11-12,373.0,370.0,370.0,366.0,366.0
2007-11-09,376.0,375.0,373.0,373.0,373.0
2007-11-08,376.0,376.0,373.0,376.0,376.0
2007-11-07,379.0,379.0,383.0,378.0,378.0
2007-11-06,374.0,374.0,374.0,379.0,379.0
2007-11-05,376.0,376.0,376.0,376.0,374.0
2007-11-02,372.0,371.0,371.0,371.0,376.0
2007-11-01,374.0,374.0,374.0,374.0,374.0
2007-10-31,369.0,369.0,371.0,372.0,372.0
2007-10-30,373.0,372.0,373.0,371.0,371.0
2007-10-29,373.0,375.0,375.0,376.0,373.0
2007-10-26,364.0,368.0,370.0,373.0,373.0
2007-10-25,360.0,360.0,360.0,364.0,368.0
2007-10-24,364.0,364.0,364.0,360.0,360.0
2007-10-23,361.0,361.0,364.0,366.0,366.0
2007-10-22,367.0,362.0,361.0,361.0,361.0
2007-10-19,,,374.0,372.0,370.0
2007-10-18,373.0,373.0,374.0,373.0,373.0
2007-10-17,372.0,372.0,370.0,373.0,373.0
2007-10-16,375.0,375.0,375.0,372.0,372.0
2007-10-15,379.0,379.0,380.0,382.0,375.0
2007-10-12,378.0,378.0,378.0,379.0,379.0
2007-10-11,375.0,375.0,376.0,381.0,384.0
2007-10-10,365.0,365.0,367.0,377.0,377.0
2007-10-09,365.0,363.0,362.0,362.0,365.0
2007-10-08,369.0,369.0,367.0,366.0,365.0
2007-10-05,369.0,369.0,371.0,369.0,369.0
2007-10-04,359.0,359.0,360.0,362.0,369.0
2007-10-03,352.0,350.0,352.0,352.0,359.0
2007-10-02,358.0,357.0,356.0,352.0,352.0
2007-10-01,,,349.0,355.0,360.0
2007-09-28,345.0,345.0,345.0,346.0,348.0
2007-09-27,342.0,342.0,342.0,343.0,345.0
2007-09-26,,,341.0,340.0,343.0
2007-09-25,342.0,341.0,343.0,341.0,341.0
2007-09-24,340.0,340.0,342.0,342.0,342.0
2007-09-21,341.0,341.0,342.0,342.0,340.0
2007-09-20,335.0,335.0,335.0,338.0,341.0
2007-09-19,333.0,333.0,335.0,335.0,335.0
2007-09-18,333.0,333.0,334.0,333.0,333.0
2007-09-17,331.0,331.0,331.0,333.0,333.0
2007-09-14,334.0,333.0,333.0,333.0,331.0
2007-09-13,336.0,336.0,336.0,334.0,334.0
2007-09-12,336.0,336.0,336.0,336.0,336.0
2007-09-11,333.0,335.0,335.0,336.0,336.0
2007-09-10,337.0,337.0,337.0,336.0,333.0
2007-09-07,336.0,336.0,338.0,337.0,337.0
2007-09-06,333.0,333.0,336.0,336.0,336.0
2007-09-05,334.0,334.0,334.0,336.0,333.0
2007-09-04,333.0,333.0,334.0,334.0,334.0
2007-09-03,334.0,334.0,335.0,334.0,
2007-08-31,331.0,333.0,334.0,333.0,333.0
2007-08-30,331.0,331.0,332.0,331.0,331.0
2007-08-29,329.0,327.0,329.0,329.0,331.0
2007-08-28,331.0,331.0,334.0,331.0,331.0
2007-08-27,330.0,331.0,331.0,331.0,331.0
2007-08-24,326.0,326.0,327.0,325.0,330.0
2007-08-23,322.0,322.0,326.0,330.0,326.0
2007-08-22,321.0,319.0,319.0,322.0,322.0
2007-08-21,331.0,331.0,329.0,328.0,325.0
2007-08-20,331.0,331.0,331.0,331.0,331.0
2007-08-17,334.0,334.0,334.0,335.0,331.0
2007-08-16,348.0,346.0,345.0,338.0,329.0
2007-08-15,354.0,354.0,352.0,348.0,348.0
2007-08-14,357.0,357.0,356.0,351.0,354.0
2007-08-13,355.0,355.0,354.0,356.0,358.0
2007-08-10,361.0,357.0,357.0,350.0,358.0
2007-08-09,364.0,364.0,364.0,361.0,361.0
2007-08-08,362.0,362.0,362.0,364.0,364.0
2007-08-07,365.0,365.0,363.0,360.0,363.0
2007-08-06,365.0,365.0,365.0,365.0,365.0
2007-08-03,366.0,366.0,365.0,365.0,367.0
2007-08-02,365.0,365.0,365.0,368.0,366.0
2007-08-01,367.0,366.0,366.0,365.0,367.0
2007-07-31,367.0,367.0,365.0,367.0,367.0
2007-07-30,363.0,362.0,361.0,365.0,367.0
2007-07-27,365.0,365.0,364.0,363.0,363.0
2007-07-26,366.0,366.0,365.0,365.0,365.0
2007-07-25,368.0,368.0,368.0,366.0,366.0
2007-07-24,372.0,372.0,372.0,370.0,368.0
2007-07-23,372.0,372.0,372.0,372.0,372.0
2007-07-20,372.0,372.0,372.0,372.0,372.0
2007-07-19,370.0,369.0,369.0,370.0,372.0
2007-07-18,368.0,368.0,367.0,367.0,370.0
2007-07-17,368.0,368.0,368.0,368.0,365.0
2007-07-16,369.0,369.0,368.0,368.0,368.0
2007-07-13,370.0,370.0,370.0,369.0,369.0
2007-07-12,369.0,369.0,368.0,370.0,370.0
2007-07-11,369.0,369.0,369.0,369.0,369.0
2007-07-10,369.0,369.0,369.0,369.0,367.0
2007-07-09,367.0,367.0,366.0,370.0,369.0
2007-07-06,366.0,366.0,365.0,365.0,367.0
2007-07-05,366.0,366.0,366.0,367.0,366.0
2007-07-04,366.0,368.0,368.0,366.0,
2007-07-03,368.0,370.0,370.0,368.0,366.0
2007-07-02,,,369.0,368.0,368.0
2007-06-29,368.0,368.0,368.0,368.0,368.0
2007-06-28,367.0,367.0,368.0,368.0,368.0
2007-06-27,366.0,366.0,366.0,368.0,364.0
2007-06-26,372.0,372.0,370.0,368.0,366.0
2007-06-25,377.0,377.0,376.0,373.0,372.0
2007-06-22,376.0,376.0,375.0,377.0,377.0
2007-06-21,375.0,375.0,374.0,376.0,376.0
2007-06-20,373.0,373.0,371.0,375.0,377.0
2007-06-19,,,372.0,371.0,371.0
2007-06-18,370.0,371.0,373.0,373.0,373.0
2007-06-15,370.0,369.0,369.0,369.0,372.0
2007-06-14,367.0,367.0,369.0,369.0,369.0
2007-06-13,369.0,369.0,367.0,365.0,369.0
2007-06-12,368.0,368.0,371.0,369.0,369.0
2007-06-11,367.0,367.0,367.0,368.0,368.0
2007-06-08,369.0,368.0,368.0,371.0,369.0
2007-06-07,370.0,370.0,370.0,369.0,371.0
2007-06-06,370.0,370.0,370.0,368.0,368.0
2007-06-05,372.0,372.0,372.0,372.0,368.0
2007-06-04,376.0,374.0,374.0,372.0,372.0
2007-06-01,370.0,370.0,370.0,373.0,373.0
2007-05-31,368.0,368.0,368.0,370.0,370.0
2007-05-30,370.0,369.0,369.0,367.0,367.0
2007-05-29,370.0,369.0,369.0,371.0,368.0
2007-05-28,368.0,368.0,368.0,,
2007-05-25,368.0,368.0,368.0,367.0,367.0
2007-05-24,,,376.0,376.0,368.0
2007-05-23,375.0,375.0,378.0,376.0,376.0
2007-05-22,374.0,374.0,374.0,378.0,378.0
2007-05-21,364.0,364.0,365.0,368.0,374.0
2007-05-18,362.0,361.0,361.0,364.0,364.0
2007-05-17,359.0,359.0,359.0,359.0,362.0
2007-05-16,363.0,363.0,362.0,362.0,359.0
2007-05-15,362.0,362.0,362.0,358.0,362.0
2007-05-14,368.0,368.0,368.0,364.0,362.0
2007-05-11,361.0,363.0,362.0,364.0,367.0
2007-05-10,370.0,370.0,366.0,363.0,363.0
2007-05-09,376.0,376.0,373.0,372.0,370.0
2007-05-08,378.0,378.0,378.0,376.0,376.0
2007-05-07,378.0,378.0,381.0,381.0,381.0
2007-05-04,376.0,374.0,374.0,376.0,376.0
2007-05-03,373.0,373.0,373.0,376.0,376.0
2007-05-02,373.0,373.0,373.0,372.0,375.0
2007-05-01,,,371.0,369.0,374.0
2007-04-30,373.0,373.0,373.0,373.0,373.0
2007-04-27,373.0,372.0,372.0,374.0,374.0
2007-04-26,380.0,380.0,380.0,376.0,373.0
2007-04-25,377.0,377.0,377.0,380.0,380.0
2007-04-24,384.0,384.0,384.0,383.0,379.0
2007-04-23,386.0,386.0,386.0,382.0,386.0
2007-04-20,378.0,378.0,378.0,385.0,387.0
2007-04-19,383.0,382.0,377.0,377.0,377.0
2007-04-18,377.0,377.0,378.0,377.0,382.0
2007-04-17,376.0,376.0,376.0,376.0,379.0
2007-04-16,380.0,381.0,381.0,376.0,376.0
2007-04-13,371.0,371.0,371.0,374.0,380.0
2007-04-12,367.0,367.0,369.0,371.0,371.0
2007-04-11,360.0,360.0,363.0,366.0,369.0
2007-04-10,358.0,358.0,360.0,360.0,360.0
2007-04-09,,,,355.0,355.0
2007-04-05,,,355.0,353.0,355.0
2007-04-04,354.0,354.0,353.0,355.0,355.0
2007-04-03,353.0,353.0,354.0,354.0,354.0
2007-04-02,355.0,355.0,355.0,353.0,355.0
2007-03-30,354.0,354.0,356.0,355.0,355.0
2007-03-29,355.0,356.0,356.0,355.0,355.0
2007-03-28,355.0,356.0,356.0,356.0,356.0
2007-03-27,355.0,355.0,357.0,355.0,355.0
2007-03-26,354.0,354.0,355.0,355.0,357.0
2007-03-23,355.0,355.0,355.0,355.0,358.0
2007-03-22,354.0,354.0,353.0,356.0,356.0
2007-03-21,352.0,352.0,352.0,352.0,350.0
2007-03-20,352.0,352.0,352.0,352.0,352.0
2007-03-19,352.0,352.0,352.0,352.0,352.0
2007-03-16,352.0,352.0,352.0,352.0,352.0
2007-03-15,349.0,349.0,349.0,352.0,352.0
2007-03-14,351.0,349.0,348.0,349.0,349.0
2007-03-13,352.0,352.0,352.0,351.0,351.0
2007-03-12,353.0,353.0,353.0,352.0,352.0
2007-03-09,353.0,351.0,353.0,353.0,353.0
2007-03-08,349.0,349.0,349.0,353.0,355.0
2007-03-07,349.0,348.0,348.0,348.0,348.0
2007-03-06,342.0,343.0,345.0,345.0,350.0
2007-03-05,344.0,342.0,340.0,340.0,345.0
2007-03-02,351.0,351.0,351.0,349.0,349.0
2007-03-01,351.0,354.0,352.0,355.0,351.0
2007-02-28,347.0,348.0,348.0,350.0,350.0
2007-02-27,357.0,356.0,356.0,351.0,356.0
2007-02-26,358.0,359.0,359.0,357.0,357.0
2007-02-23,347.0,348.0,348.0,355.0,360.0
2007-02-22,346.0,346.0,346.0,350.0,350.0
2007-02-21,339.0,339.0,340.0,339.0,346.0
2007-02-20,,,342.0,337.0,337.0
2007-02-19,,,343.0,342.0,342.0
2007-02-16,344.0,343.0,343.0,340.0,343.0
2007-02-15,345.0,343.0,343.0,344.0,344.0
2007-02-14,343.0,343.0,343.0,345.0,347.0
2007-02-13,340.0,339.0,339.0,339.0,343.0
2007-02-12,338.0,338.0,340.0,338.0,340.0
2007-02-09,343.0,343.0,343.0,338.0,342.0
2007-02-08,344.0,344.0,344.0,339.0,342.0
2007-02-07,344.0,346.0,345.0,346.0,346.0
2007-02-06,340.0,340.0,342.0,344.0,344.0
2007-02-05,337.0,336.0,336.0,340.0,343.0
2007-02-02,344.0,344.0,343.0,341.0,341.0
2007-02-01,341.0,341.0,341.0,344.0,344.0
2007-01-31,341.0,340.0,340.0,334.0,341.0
2007-01-30,343.0,341.0,343.0,336.0,342.0
2007-01-29,349.0,349.0,350.0,342.0,346.0
2007-01-26,353.0,352.0,351.0,351.0,351.0
2007-01-25,350.0,350.0,350.0,353.0,353.0
2007-01-24,351.0,350.0,350.0,348.0,348.0
2007-01-23,345.0,345.0,347.0,350.0,350.0
2007-01-22,343.0,343.0,343.0,344.0,347.0
2007-01-19,340.0,340.0,341.0,341.0,344.0
2007-01-18,340.0,342.0,342.0,342.0,342.0
2007-01-17,335.0,335.0,333.0,334.0,343.0
2007-01-16,332.0,332.0,332.0,334.0,337.0
2007-01-15,334.0,336.0,335.0,332.0,332.0
2007-01-12,331.0,331.0,331.0,331.0,335.0
2007-01-11,331.0,331.0,331.0,333.0,333.0
2007-01-10,333.0,333.0,334.0,331.0,331.0
2007-01-09,333.0,333.0,336.0,329.0,329.0
2007-01-08,335.0,335.0,335.0,333.0,333.0
2007-01-05,340.0,340.0,340.0,342.0,336.0
2007-01-04,337.0,337.0,337.0,340.0,343.0
2007-01-03,338.0,336.0,336.0,342.0,342.0
2007-01-02,337.0,337.0,334.0,336.0,336.0
2006-12-29,327.0,327.0,327.0,327.0,337.0
2006-12-28,326.0,326.0,328.0,327.0,326.0
2006-12-27,326.0,328.0,328.0,328.0,326.0
2006-12-26,,,,327.0,327.0
2006-12-22,325.0,325.0,327.0,327.0,327.0
2006-12-21,326.0,326.0,327.0,325.0,325.0
2006-12-20,328.0,328.0,328.0,326.0,326.0
2006-12-19,324.0,324.0,325.0,322.0,326.0
2006-12-18,325.0,325.0,326.0,324.0,324.0
2006-12-15,330.0,329.0,329.0,327.0,325.0
2006-12-14,328.0,328.0,328.0,330.0,330.0
2006-12-13,329.0,329.0,330.0,328.0,328.0
2006-12-12,332.0,332.0,332.0,329.0,329.0
2006-12-11,329.0,329.0,329.0,329.0,329.0
2006-12-08,330.0,329.0,329.0,332.0,336.0
2006-12-07,328.0,326.0,326.0,328.0,328.0
2006-12-06,333.0,331.0,331.0,328.0,328.0
2006-12-05,330.0,330.0,329.0,333.0,333.0
2006-12-04,330.0,330.0,330.0,330.0,330.0
2006-12-01,330.0,330.0,330.0,328.0,328.0
2006-11-30,324.0,323.0,323.0,330.0,330.0
2006-11-29,326.0,326.0,328.0,321.0,321.0
2006-11-28,329.0,328.0,328.0,326.0,326.0
2006-11-27,330.0,329.0,329.0,329.0,329.0
2006-11-24,326.0,326.0,326.0,330.0,
2006-11-23,328.0,328.0,327.0,326.0,
2006-11-22,330.0,330.0,328.0,328.0,328.0
2006-11-21,323.0,327.0,327.0,330.0,330.0
2006-11-20,320.0,320.0,322.0,323.0,323.0
2006-11-17,321.0,321.0,321.0,318.0,320.0
2006-11-16,320.0,320.0,322.0,323.0,323.0
2006-11-15,321.0,321.0,321.0,317.0,320.0
2006-11-14,326.0,325.0,324.0,324.0,321.0
2006-11-13,333.0,333.0,333.0,326.0,326.0
2006-11-10,338.0,338.0,338.0,335.0,333.0
2006-11-09,329.0,329.0,328.0,331.0,338.0
2006-11-08,333.0,333.0,334.0,327.0,327.0
2006-11-07,334.0,332.0,332.0,335.0,335.0
2006-11-06,340.0,340.0,340.0,330.0,335.0
2006-11-03,326.0,326.0,325.0,330.0,333.0
2006-11-02,327.0,326.0,326.0,324.0,326.0
2006-11-01,323.0,323.0,324.0,326.0,326.0
2006-10-31,325.0,325.0,325.0,318.0,323.0
2006-10-30,,,325.0,325.0,325.0
2006-10-27,324.0,324.0,324.0,321.0,323.0
2006-10-26,325.0,324.0,324.0,323.0,326.0
2006-10-25,322.0,322.0,322.0,319.0,319.0
2006-10-24,319.0,318.0,318.0,320.0,323.0
2006-10-23,326.0,326.0,326.0,319.0,319.0
2006-10-20,337.0,337.0,334.0,329.0,329.0
2006-10-19,331.0,331.0,331.0,330.0,337.0
2006-10-18,320.0,320.0,320.0,326.0,334.0
2006-10-17,324.0,326.0,326.0,321.0,321.0
2006-10-16,318.0,321.0,320.0,324.0,324.0
2006-10-13,309.0,309.0,309.0,316.0,316.0
2006-10-12,305.0,308.0,308.0,310.0,310.0
2006-10-11,299.0,299.0,301.0,305.0,309.0
2006-10-10,304.0,308.0,308.0,299.0,299.0
2006-10-09,302.0,302.0,304.0,304.0,304.0
2006-10-06,301.0,301.0,301.0,297.0,297.0
2006-10-05,297.0,299.0,299.0,301.0,301.0
2006-10-04,300.0,298.0,298.0,302.0,297.0
2006-10-03,315.0,315.0,314.0,305.0,305.0
2006-10-02,,,322.0,315.0,315.0
2006-09-29,321.0,323.0,323.0,318.0,318.0
2006-09-28,320.0,323.0,323.0,323.0,323.0
2006-09-27,318.0,318.0,320.0,317.0,320.0
2006-09-26,318.0,318.0,319.0,318.0,318.0
2006-09-25,319.0,318.0,319.0,316.0,316.0
2006-09-22,310.0,310.0,313.0,325.0,322.0
2006-09-21,308.0,308.0,308.0,309.0,309.0
2006-09-20,307.0,307.0,308.0,311.0,311.0
2006-09-19,317.0,316.0,316.0,319.0,310.0
2006-09-18,313.0,313.0,313.0,306.0,312.0
2006-09-15,311.0,311.0,314.0,315.0,315.0
2006-09-14,317.0,317.0,317.0,332.0,326.0
2006-09-13,310.0,310.0,310.0,321.0,318.0
2006-09-12,311.0,323.0,322.0,320.0,314.0
2006-09-11,330.0,322.0,321.0,317.0,317.0
2006-09-08,347.0,345.0,345.0,323.0,330.0
2006-09-07,350.0,350.0,353.0,348.0,348.0
2006-09-06,351.0,351.0,351.0,351.0,356.0
2006-09-05,347.0,347.0,347.0,351.0,351.0
2006-09-04,346.0,346.0,347.0,346.0,
2006-09-01,348.0,345.0,346.0,346.0,346.0
2006-08-31,340.0,340.0,342.0,343.0,343.0
2006-08-30,339.0,341.0,340.0,339.0,340.0
2006-08-29,341.0,343.0,342.0,338.0,340.0
2006-08-28,345.0,345.0,345.0,345.0,345.0
2006-08-25,345.0,345.0,345.0,346.0,346.0
2006-08-24,345.0,345.0,347.0,348.0,348.0
2006-08-23,340.0,340.0,340.0,345.0,345.0
2006-08-22,347.0,347.0,346.0,340.0,340.0
2006-08-21,335.0,338.0,338.0,341.0,347.0
2006-08-18,332.0,334.0,333.0,335.0,335.0
2006-08-17,333.0,337.0,338.0,341.0,337.0
2006-08-16,326.0,325.0,324.0,334.0,337.0
2006-08-15,317.0,320.0,319.0,322.0,327.0
2006-08-14,320.0,320.0,320.0,314.0,319.0
2006-08-11,320.0,320.0,322.0,324.0,324.0
2006-08-10,326.0,326.0,327.0,326.0,324.0
2006-08-09,320.0,320.0,320.0,324.0,327.0
2006-08-08,327.0,325.0,324.0,320.0,320.0
2006-08-07,327.0,327.0,328.0,324.0,324.0
2006-08-04,324.0,324.0,324.0,327.0,327.0
2006-08-03,330.0,326.0,327.0,324.0,324.0
2006-08-02,319.0,319.0,322.0,325.0,330.0
2006-08-01,316.0,316.0,316.0,319.0,319.0
2006-07-31,315.0,315.0,317.0,313.0,316.0
2006-07-28,320.0,318.0,318.0,315.0,315.0
2006-07-27,315.0,315.0,318.0,320.0,320.0
2006-07-26,315.0,315.0,315.0,315.0,315.0
2006-07-25,314.0,314.0,315.0,314.0,317.0
2006-07-24,309.0,309.0,309.0,309.0,314.0
2006-07-21,308.0,311.0,310.0,310.0,310.0
2006-07-20,317.0,315.0,316.0,315.0,315.0
2006-07-19,308.0,308.0,311.0,311.0,318.0
2006-07-18,320.0,320.0,319.0,318.0,316.0
2006-07-17,333.0,333.0,333.0,321.0,321.0
2006-07-14,331.0,331.0,331.0,331.0,331.0
2006-07-13,330.0,328.0,328.0,331.0,331.0
2006-07-12,330.0,330.0,330.0,330.0,330.0
2006-07-11,318.0,320.0,323.0,326.0,330.0
2006-07-10,325.0,323.0,323.0,320.0,320.0
2006-07-07,329.0,329.0,329.0,327.0,327.0
2006-07-06,328.0,324.0,326.0,323.0,329.0
2006-07-05,328.0,328.0,330.0,328.0,328.0
2006-07-04,325.0,328.0,327.0,326.0,
2006-07-03,322.0,326.0,326.0,329.0,
2006-06-30,320.0,320.0,320.0,316.0,322.0
2006-06-29,309.0,309.0,307.0,314.0,314.0
2006-06-28,310.0,310.0,313.0,314.0,314.0
2006-06-27,318.0,320.0,320.0,318.0,318.0
2006-06-26,308.0,305.0,309.0,320.0,320.0
2006-06-23,310.0,304.0,305.0,306.0,310.0
2006-06-22,315.0,318.0,320.0,320.0,316.0
2006-06-21,303.0,306.0,308.0,311.0,315.0
2006-06-20,292.0,297.0,296.0,301.0,305.0
2006-06-19,307.0,304.0,303.0,302.0,297.0
2006-06-16,300.0,306.0,305.0,310.0,307.0
2006-06-15,290.0,290.0,292.0,300.0,300.0
2006-06-14,277.0,274.0,275.0,288.0,293.0
2006-06-13,313.0,308.0,307.0,286.0,277.0
2006-06-12,320.0,320.0,316.0,321.0,316.0
2006-06-09,317.0,313.0,313.0,327.0,327.0
2006-06-08,342.0,336.0,333.0,331.0,320.0
2006-06-07,348.0,346.0,346.0,335.0,343.0
2006-06-06,359.0,359.0,359.0,350.0,350.0
2006-06-05,356.0,356.0,358.0,363.0,363.0
2006-06-02,340.0,343.0,342.0,351.0,356.0
2006-06-01,347.0,345.0,345.0,340.0,340.0
2006-05-31,,,358.0,358.0,345.0
2006-05-30,352.0,350.0,355.0,359.0,358.0
2006-05-29,357.0,352.0,350.0,,
2006-05-26,355.0,353.0,354.0,354.0,354.0
2006-05-25,348.0,348.0,350.0,350.0,350.0
2006-05-24,358.0,362.0,365.0,352.0,352.0
2006-05-23,343.0,342.0,343.0,355.0,362.0
2006-05-22,350.0,345.0,345.0,340.0,340.0
2006-05-19,366.0,369.0,373.0,347.0,352.0
2006-05-18,372.0,375.0,376.0,380.0,375.0
2006-05-17,379.0,379.0,382.0,390.0,380.0
2006-05-16,368.0,370.0,366.0,379.0,379.0
2006-05-15,395.0,395.0,397.0,370.0,375.0
2006-05-12,400.0,396.0,398.0,407.0,399.0
2006-05-11,390.0,397.0,395.0,400.0,400.0
2006-05-10,394.0,397.0,398.0,390.0,390.0
2006-05-09,375.0,375.0,378.0,384.0,394.0
2006-05-08,380.0,380.0,381.0,377.0,375.0
2006-05-05,,,383.0,382.0,382.0
2006-05-04,379.0,379.0,378.0,379.0,379.0
2006-05-03,386.0,386.0,388.0,384.0,379.0
2006-05-02,377.0,377.0,380.0,380.0,384.0
2006-05-01,,,,380.0,380.0
2006-04-28,360.0,363.0,363.0,364.0,377.0
2006-04-27,368.0,365.0,367.0,364.0,364.0
2006-04-26,366.0,366.0,367.0,361.0,368.0
2006-04-25,356.0,355.0,355.0,362.0,362.0
2006-04-24,359.0,359.0,363.0,360.0,360.0
2006-04-21,344.0,348.0,347.0,352.0,359.0
2006-04-20,368.0,372.0,374.0,365.0,349.0
2006-04-19,366.0,364.0,364.0,371.0,374.0
2006-04-18,364.0,360.0,360.0,361.0,361.0
2006-04-17,,,,358.0,358.0
2006-04-13,347.0,342.0,341.0,346.0,349.0
2006-04-12,340.0,344.0,343.0,347.0,347.0
2006-04-11,359.0,359.0,360.0,359.0,345.0
2006-04-10,351.0,354.0,355.0,359.0,359.0
2006-04-07,352.0,352.0,354.0,351.0,351.0
2006-04-06,341.0,341.0,344.0,352.0,352.0
2006-04-05,,,336.0,341.0,341.0
2006-04-04,342.0,339.0,337.0,338.0,342.0
2006-04-03,332.0,337.0,338.0,341.0,345.0
2006-03-31,349.0,349.0,348.0,332.0,332.0
2006-03-30,338.0,341.0,343.0,349.0,349.0
2006-03-29,340.0,337.0,337.0,333.0,338.0
2006-03-28,340.0,344.0,345.0,340.0,340.0
2006-03-27,333.0,333.0,334.0,341.0,341.0
2006-03-24,321.0,321.0,320.0,326.0,333.0
2006-03-23,323.0,321.0,321.0,317.0,322.0
2006-03-22,317.0,318.0,322.0,320.0,324.0
2006-03-21,320.0,318.0,316.0,315.0,318.0
2006-03-20,318.0,318.0,319.0,317.0,317.0
2006-03-17,316.0,316.0,315.0,318.0,318.0
2006-03-16,315.0,314.0,314.0,316.0,316.0
2006-03-15,305.0,305.0,307.0,318.0,318.0
2006-03-14,300.0,300.0,300.0,302.0,306.0
2006-03-13,288.0,291.0,290.0,292.0,300.0
2006-03-10,289.0,289.0,289.0,288.0,288.0
2006-03-09,280.0,282.0,282.0,285.0,285.0
2006-03-08,291.0,289.0,289.0,285.0,282.0
2006-03-07,296.0,296.0,296.0,299.0,292.0
2006-03-06,307.0,304.0,302.0,302.0,297.0
2006-03-03,300.0,300.0,300.0,305.0,305.0
2006-03-02,297.0,297.0,296.0,294.0,300.0
2006-03-01,291.0,291.0,289.0,290.0,297.0
2006-02-28,284.0,284.0,285.0,288.0,291.0
2006-02-27,286.0,290.0,290.0,285.0,284.0
2006-02-24,283.0,285.0,286.0,286.0,286.0
2006-02-23,289.0,286.0,287.0,288.0,286.0
2006-02-22,293.0,293.0,293.0,292.0,289.0
2006-02-21,292.0,290.0,291.0,291.0,293.0
2006-02-20,292.0,292.0,292.0,292.0,292.0
2006-02-17,279.0,279.0,280.0,285.0,290.0
2006-02-16,276.0,276.0,278.0,275.0,279.0
2006-02-15,282.0,285.0,287.0,285.0,279.0
2006-02-14,273.0,270.0,274.0,278.0,282.0
2006-02-13,283.0,278.0,277.0,282.0,276.0
2006-02-10,304.0,298.0,297.0,296.0,285.0
2006-02-09,293.0,297.0,295.0,300.0,300.0
2006-02-08,288.0,288.0,287.0,290.0,290.0
2006-02-07,309.0,309.0,309.0,297.0,290.0
2006-02-06,317.0,317.0,320.0,305.0,312.0
2006-02-03,309.0,310.0,310.0,317.0,317.0
2006-02-02,294.0,296.0,295.0,300.0,305.0
2006-02-01,294.0,293.0,293.0,294.0,294.0
2006-01-31,,,282.0,293.0,295.0
2006-01-30,,,277.0,278.0,278.0
2006-01-27,275.0,275.0,276.0,275.0,275.0
2006-01-26,279.0,279.0,280.0,275.0,275.0
2006-01-25,275.0,275.0,275.0,279.0,279.0
2006-01-24,278.0,278.0,278.0,276.0,276.0
2006-01-23,276.0,278.0,277.0,278.0,278.0
2006-01-20,279.0,278.0,277.0,280.0,277.0
2006-01-19,273.0,275.0,275.0,273.0,277.0
2006-01-18,282.0,276.0,275.0,273.0,273.0
2006-01-17,289.0,286.0,286.0,281.0,283.0
2006-01-16,283.0,285.0,285.0,289.0,289.0
2006-01-13,273.0,273.0,273.0,275.0,281.0
2006-01-12,274.0,274.0,274.0,273.0,273.0
2006-01-11,274.0,274.0,274.0,271.0,274.0
2006-01-10,279.0,278.0,278.0,277.0,274.0
2006-01-09,272.0,272.0,274.0,275.0,278.0
2006-01-06,264.0,265.0,262.0,269.0,272.0
2006-01-05,274.0,274.0,272.0,263.0,263.0
2006-01-04,272.0,272.0,272.0,272.0,274.0
2006-01-03,260.0,262.0,262.0,267.0,267.0
""".strip()

FETCHER_UNIVERSE_DATA = """
date,symbol
1/9/2006,aapl
1/9/2006,ibm
1/9/2006,msft
1/11/2006,aapl
1/11/2006,ibm
1/11/2006,msft
1/11/2006,yhoo
""".strip()

NON_ASSET_FETCHER_UNIVERSE_DATA = """
date,symbol
1/9/2006,foobarbaz
1/9/2006,bazfoobar
1/9/2006,barbazfoo
1/11/2006,foobarbaz
1/11/2006,bazfoobar
1/11/2006,barbazfoo
1/11/2006,foobarbaz
""".strip()

FETCHER_ALTERNATE_COLUMN_HEADER = "ARGLEBARGLE"
FETCHER_UNIVERSE_DATA_TICKER_COLUMN = FETCHER_UNIVERSE_DATA.replace(
    "symbol", FETCHER_ALTERNATE_COLUMN_HEADER)
