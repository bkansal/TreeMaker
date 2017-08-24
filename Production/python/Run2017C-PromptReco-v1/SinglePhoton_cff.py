import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/368/00000/424693F6-876D-E711-8723-02163E01A3EC.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/368/00000/C806D1A0-956D-E711-8F5D-02163E0128EA.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/369/00000/16389E1D-A96D-E711-8CBD-02163E011E1F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/369/00000/24246AD8-9B6D-E711-A1FE-02163E01338A.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/369/00000/B000A1E2-976D-E711-9D4E-02163E014614.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/369/00000/C62C06F6-A06D-E711-8ECA-02163E01A20F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/369/00000/D2EBB6AE-946D-E711-BB23-02163E014498.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/0080DCC3-F56E-E711-A502-02163E014161.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/2007D4A5-CB6D-E711-A878-02163E011DAE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/20A7ED55-C66D-E711-B7D5-02163E019C2A.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/2E418A7C-C96D-E711-9267-02163E01A342.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/4AD91808-BF6D-E711-AB32-02163E01A759.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/809A6E63-C16D-E711-8203-02163E0142F6.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/A205D748-C36D-E711-A0CD-02163E01A3A0.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/C07913CE-C46D-E711-8E53-02163E0145C8.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/370/00000/EC1D0CBC-946E-E711-A0D0-02163E019E5B.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/380/00000/3AE6762C-E56D-E711-B671-02163E01A3C2.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/380/00000/4885EA6E-F06D-E711-BEFA-02163E011C47.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/380/00000/54F0FE80-DF6D-E711-A250-02163E013390.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/381/00000/28D3104B-F26D-E711-874D-02163E019D4C.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/394/00000/EC4B7062-2A6E-E711-937A-02163E0138FB.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/395/00000/3A3F5991-0D6E-E711-B416-02163E01A39A.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/395/00000/62E64E5A-2A6E-E711-866B-02163E011F59.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/395/00000/A006F975-156E-E711-9987-02163E014242.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/396/00000/34C2202D-146E-E711-AF0D-02163E019B4F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/414/00000/3C94BDB6-0E6E-E711-83F3-02163E019D5F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/420/00000/7ECE5E2F-466E-E711-93E5-02163E01A363.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/443/00000/98F4D6E8-9F70-E711-9F9C-02163E01A594.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/443/00000/9C3172C3-A770-E711-B3F6-02163E0142FA.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/443/00000/C841D28C-5F71-E711-9517-02163E0141EE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/450/00000/9C689DE1-BD70-E711-963F-02163E0140FE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/477/00000/90CB1B12-A970-E711-8985-02163E01424D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/478/00000/5C6ACC75-2971-E711-B35A-02163E019CDD.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/478/00000/B27E44ED-9D70-E711-A9F4-02163E0138B2.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/478/00000/DE9D98BE-A570-E711-85C7-02163E0133E6.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/479/00000/6AC383A1-3471-E711-A075-02163E0138DD.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/479/00000/92DAD052-A770-E711-9242-02163E01A333.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/14992361-A670-E711-A9D5-02163E01A38C.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/228805CA-B370-E711-8C92-02163E01A5B3.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/5EA87C28-A570-E711-9783-02163E01A3F0.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/869DBC9F-A870-E711-AE10-02163E019C61.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/92FD48AA-A070-E711-BF54-02163E01A30E.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/CA7CE4E3-AA70-E711-B9FF-02163E01A38C.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/CEEF193D-1D71-E711-BCF6-02163E0144A2.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/D47747DE-9D70-E711-BB53-02163E0135A0.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/E8C8D49E-AE70-E711-8A9F-02163E013967.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/F20E49CE-A170-E711-BB8A-02163E01209F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/480/00000/FA1C95D8-A370-E711-9B23-02163E01A3F3.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/0C7EBF15-C470-E711-93E9-02163E019BA3.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/1A0E02F1-C170-E711-ADBA-02163E011C13.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/1CC90552-C370-E711-AD84-02163E01350F.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/22AF8E15-CC70-E711-B430-02163E0145B4.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/5A168814-C670-E711-8BEF-02163E01A6D4.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/5CA66272-DD70-E711-97D9-02163E019C91.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/6076FBC0-BD70-E711-B0EA-02163E0139CA.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/86C4BFE5-BF70-E711-9997-02163E0143DC.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/8C40D52D-C770-E711-AC71-02163E01A61E.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/8E86FB9E-C970-E711-A489-02163E019B3E.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/A0CD0476-BD70-E711-8F16-02163E01A3EC.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/A43B91A3-E170-E711-A81C-02163E0135EF.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/A8346685-BA70-E711-87F5-02163E0141FC.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/AAEE3C05-C170-E711-8D6C-02163E01A30D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/BC410F80-BE70-E711-9F67-02163E0141FC.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/481/00000/DA496332-D370-E711-8F89-02163E01A6E9.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/592/00000/583E8B58-F970-E711-AF47-02163E019DE3.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/592/00000/86E51F5A-ED70-E711-AE68-02163E019E84.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/168A87BE-FB70-E711-94E4-02163E019B31.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/2A184C77-FA70-E711-B56F-02163E013931.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/2CC0208C-FD70-E711-B662-02163E014168.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/48EEAC64-FE70-E711-98A2-02163E01A40C.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/66C7C1C0-F570-E711-BF6F-02163E011A33.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/7E12E60F-6A71-E711-BD13-02163E01A28D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/A480D91C-0871-E711-9364-02163E019E5D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/B81EF864-0371-E711-94C0-02163E01A28D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/DA8F37A4-0071-E711-B9E8-02163E01A511.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/E0210114-0C71-E711-A4B2-02163E011911.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/593/00000/FC8AED37-F970-E711-93D1-02163E01A1E1.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/594/00000/2CDB9B11-3271-E711-8223-02163E019C22.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/594/00000/4AE6A045-2A71-E711-8D74-02163E0142F0.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/594/00000/C88AA4C7-2C71-E711-9048-02163E011C49.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/594/00000/FAE0F5B0-3C71-E711-8B59-02163E01A739.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/595/00000/08FE7A51-3771-E711-9125-02163E019C22.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/595/00000/B85E712E-3071-E711-8FA3-02163E019DA7.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/597/00000/108EF838-3571-E711-BF3C-02163E0127E4.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/597/00000/2C8919DB-3771-E711-B1FE-02163E01A5BE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/597/00000/6E790303-3A71-E711-B305-02163E011948.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/597/00000/CA66B660-3071-E711-A735-02163E011D12.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/597/00000/D66FEECD-3E71-E711-9F59-02163E011A03.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/598/00000/7E5C1F04-2F71-E711-8D96-02163E014184.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/614/00000/268E2B8E-5571-E711-AE3A-02163E019E77.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/614/00000/C0AAE864-6071-E711-A398-02163E014498.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/614/00000/E46311FF-4771-E711-B3BA-02163E01A6D6.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/614/00000/E47038E1-5971-E711-A14A-02163E011DAE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/614/00000/F25FAD80-4D71-E711-B74F-02163E01A4E2.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/0C2AF433-5671-E711-97D3-02163E01410E.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/34A3FA2C-4C71-E711-A8C1-02163E014148.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/64D69D0A-6871-E711-8E08-02163E01A28D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/68C16A64-4871-E711-B7D5-02163E011E01.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/6A168C14-4D71-E711-8398-02163E0142FA.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/84B02C3B-4A71-E711-B349-02163E01466D.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/AC62B7AD-4571-E711-A480-02163E011F67.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/D23416D9-4F71-E711-8754-02163E012644.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/616/00000/E25DE4B1-5171-E711-9B36-02163E011A23.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/617/00000/1ED0BF2F-6371-E711-9BBE-02163E014434.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/617/00000/FCB17A34-6671-E711-A2C5-02163E01A231.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/5C378AAC-DA71-E711-B16D-02163E01A605.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/5E2C0355-D171-E711-BE78-02163E019D58.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/7C82F3E4-D271-E711-B5C6-02163E01A599.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/A05646C0-E371-E711-9043-02163E0120B5.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/B2E06721-F771-E711-91E8-02163E011DEE.root',
'/store/data/Run2017C/SinglePhoton/MINIAOD/PromptReco-v1/000/299/649/00000/FAE659EE-D571-E711-B678-02163E019DD3.root' ] );