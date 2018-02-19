#Solution MSI LIST to check for files and make sure we have them all for copy and sign and rename funcitons
MSILIST = {
	'MSICOMB_LIST' : [
			'AssetManagementCombine_x64.msi',
			'CMDBCombine_x64.msi',
			'InventoryCombine_x64.msi',
			'PatchManagementCombine_x64.msi',
			'SoftwareManagementCombine_x64.msi',
			],
			
	'AC_LIST' : [ 
			'ActivityCenter_x64.msi',
			'ActivityCenterLanguages_x64.msi',
			],

	'AM_CMDB_RP_LIST' : [
		'AssetLanguages_x64.msi',
		'AssetManagement_x64.msi',
		'AssetReports_x64.msi',
		'AssetUpgrade_x64.msi',
		'AssetUpgrade_x86.msi',
		'CMDB_x64.msi',
		'CMDBLanguages_x64.msi',
		'CMDBReports_x64.msi',
		'CMDBUpgrade_x64.msi',
		'CMDBUpgrade_x86.msi',
		'ResourcePlatform_x64.msi',
		'ResourcePlatformLanguages_x64.msi',
		],

	'DS_LIST' : [
		'DeploymentSolution_x64.msi',
		'DeploymentSolutionLanguages_x64.msi',
		'DeploymentSolutionLINUX_x64.msi',
		],

	'EC_LIST' : [
		'EventConsole_x64.msi',
		'EventConsoleLanguages_x64.msi',
		],
	
	'FTS_LIST' : [
		'SetupPortal_x64.msi'
		],

	'IS_LIST' : [
		'AgentlessInventoryReports_x64.msi',
		'AgentlessInventoryReports_x86.msi',
		'AgentlessInventoryUpgrade_x64.msi',
		'AgentlessInventoryUpgrade_x86.msi',
		'Inventorypackforservers_x64.msi',
		'Inventorypackforserverslanguages_x64.msi',
		'Inventorypackforserversupgradelanguages_x86.msi',
		'Inventorypackforserversupgradelanguages_x64.msi',
		'Inventorypackforserverupgrade_x64.msi',
		'Inventorypackforserverupgrade_x86.msi',
		'Inventorysolution_x64.msi',
		'Inventorysolutionlanguages_x64.msi',
		'Inventorysolutionupgrade_x64.msi',
		'Inventorysolutionupgrade_x86.msi',
		'Inventorysolutionupgradelanguages_x64.msi',
		'Inventorysolutionupgradelanguages_x86.msi',
		'NetworkInventoryTask_x64.msi',
		'NetworkInventoryTask_x86.msi',
		'NetworkInventoryTaskLanguages_x64.msi',
		'NetworkInventoryTaskLanguages_x86.msi',
		'Softwarecatalogdataprovider_x64.msi',
		'Softwarecatalogdataproviderlanguages_x64.msi',
		],

	'ISPACK_LIST' : [
		'InventoryPackForServersUnix_x64.msi',
		'InventoryPackForServersUnixLanguages_x64.msi',
		],

	'ULMIS_LIST' : [	
		'Inventorysolutionunix_x64.msi',
		'InventorysolutionunixLanguages_x64.msi',
		],

	'MC_LIST' : [
		'MonitorAgentUnix_x64.msi',
		'MonitorAgentUnixLanguages_x64.msi',
		'MonitorAgentWindows_x64.msi',
		'MonitorAgentWindowsLanguages_x64.msi',
		'MonitorCore_x64.msi',
		'MonitorCoreLanguages_x64.msi',
		'MonitorUpgrade_x64.msi',
		'MonitorUpgrade_x86.msi',
		],
	
	'MP_LIST' : [
		'MonitorPackServers_x64.msi',
		'MonitorPackServersLanguages_x64.msi',
		],

	'OOB_LIST' : [
		'OOB_x64.msi',
		'OOBLanguages_x64.msi',
		'OOBUpgrade_x64.msi',
		'OOBUpgrade_x86.msi',
		'OOBUpgradeLanguages_x64.msi',
		'OOBUpgradeLanguages_x86.msi',
		],
	
	# PCA : [
		# 'pcANS.msi',
		# 'Symantec_pcanywheresolution_12_6_x64.msi',
		# 'Symantec_pcanywheresolution_12_6_x86.msi',
		# 'symantec_pcanywheresolutionlanguages_12_6_x64.msi',
		# 'symantec_pcanywheresolutionlanguages_12_6_x86.msi',
		# ],
	
	'PM_LIST' : [
		'PatchManagementCore_x64.msi',
		'PatchManagementCoreLanguages_x64.msi',
		'PatchManagementCoreUpgrade_x64.msi',
		'PatchManagementCoreUpgrade_x86.msi',
		'PatchManagementCoreUpgradeLanguages_x64.msi',
		'PatchManagementCoreUpgradeLanguages_x86.msi',
		'PatchManagementLinux_x64.msi',
		'PatchManagementLinuxLanguages_x64.msi',
		'PatchManagementMac_x64.msi',
		'PatchManagementMacLanguages_x64.msi',
		'PatchManagementWindows_x64.msi',
		'PatchManagementWindowsLanguages_x64.msi',
		'PatchManagementWindowsUpgrade_x64.msi',
		'PatchManagementWindowsUpgrade_x86.msi',
		'PatchManagementWindowsUpgradeLanguages_x64.msi',
		'PatchManagementWindowsUpgradeLanguages_x86.msi',
		],
	
	'PS_LIST' : [
		'PowerSchemeLanguages_x64.msi',
		'PowerSchemeTask_x64.msi',
		],
	
	'RTSM_LIST' : [
		'RTCI_x64.msi',
		'RTCILanguages_x64.msi',
		'RTCIUpgrade_x64.msi',
		'RTCIUpgrade_x86.msi',
		'RTCIUpgradeLanguages_x64.msi',
		'RTCIUpgradeLanguages_x86.msi',
		'RTSM_x64.msi',
		'RTSMLanguages_x64.msi',
		'RTSMUpgrade_x64.msi',
		'RTSMUpgrade_x86.msi',
		'RTSMUpgradeLanguages_x64.msi',
		'RTSMUpgradeLanguages_x86.msi',
		],

	'SD_LIST' : [
		'ServiceDesk_x64.msi',
		'ServiceDeskLanguages_x64.msi',
		],

	'SM_LIST' : [
		'SoftwareManagementSolution_x64.msi',
		'SoftwareManagementSolutionLanguages_x64.msi',
		'SoftwarePortalLanguages_x64.msi',
		'SoftwareManagementSolutionUpgrade_x64.msi',
		'SoftwareManagementSolutionUpgrade_x86.msi',
		'SoftwareManagementSolutionUpgradeLanguages_x64.msi',
		'SoftwareManagementSolutionUpgradeLanguages_x86.msi',
		],
	
	'SMSP_LIST' : [
		'ServerManagementSuite_x64.msi',
		'ServerManagementSuiteLanguages_x64.msi',
		],

	'TOP_LIST' : [
		'TopologyView_x64.msi',
		'TopologyViewLanguages_x64.msi',
		],

	'VMM_LIST' : [
		'VMM_x64.msi',
		'VMMLanguages_x64.msi',
		],

	# WC : [
		# 'altiris_wpsprovider_7_1_x64.msi':'altiris_wpsprovider_8_0_x64.msi',
		# 'altiris_wpsprovider_7_1_x86.msi':'altiris_wpsprovider_8_0_x86.msi',
		# 'Altiris_WPSProviderLP_7_1_x64.msi':'altiris_wpsproviderlp_8_0_x64.msi',
		# 'Altiris_WPSProviderLP_7_1_x86.msi':'altiris_wpsproviderlp_8_0_x86.msi',
		# ],
	}