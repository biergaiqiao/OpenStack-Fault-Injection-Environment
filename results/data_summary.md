# Fault Injection Dataset Summary

This report provides quick statistics for the OpenStack fault injection data in the `data/` directory.

Total tests across all subsystems: **911**.

## Visual summaries

* Total tests per subsystem: `figures/subsystem_totals.svg`
* Overall fault-type distribution (top 15): `figures/overall_fault_types.svg`
* Cinder fault-type distribution: `figures/cinder_fault_types.svg`
* Cinder top 10 target components: `figures/cinder_components.svg`
* Cinder top fault-type ↔ component pairs: `figures/cinder_fault_component_pairs.svg`
* Cinder components with diverse fault types: `figures/cinder_component_diversity.svg`
* Neutron fault-type distribution: `figures/neutron_fault_types.svg`
* Neutron top 10 target components: `figures/neutron_components.svg`
* Neutron top fault-type ↔ component pairs: `figures/neutron_fault_component_pairs.svg`
* Neutron components with diverse fault types: `figures/neutron_component_diversity.svg`
* Nova fault-type distribution: `figures/nova_fault_types.svg`
* Nova top 10 target components: `figures/nova_components.svg`
* Nova top fault-type ↔ component pairs: `figures/nova_fault_component_pairs.svg`
* Nova components with diverse fault types: `figures/nova_component_diversity.svg`

---

## Cinder

* Total tests: **269**
* Unique target components: **31**
* Unique target classes: **30**
* Unique target functions: **99**

### Fault types
| Item | Count |
| --- | ---: |
| OPENSTACK_WRONG_RETURN_VALUE-VOLUME | 81 |
| OPENSTACK_MISSING_FUNCTION_CALL-VOLUME | 48 |
| OPENSTACK_THROW_EXCEPTION-VOLUME | 36 |
| OPENSTACK_WRONG_PARAMETERS-VOLUME | 35 |
| OPENSTACK_MISSING_PARAMETERS-VOLUME | 34 |
| OPENSTACK_WRONG_RETURN_VALUE-IMAGE | 12 |
| OPENSTACK_MISSING_FUNCTION_CALL-IMAGE | 7 |
| OPENSTACK_WRONG_PARAMETERS-IMAGE | 5 |
| OPENSTACK_MISSING_PARAMETERS-IMAGE | 4 |
| OPENSTACK_THROW_EXCEPTION-IMAGE | 4 |
| OPENSTACK_WRONG_RETURN_VALUE-INSTANCE | 2 |
| OPENSTACK_WRONG_RETURN_VALUE-RPC | 1 |

### Top 5 target components
| Item | Count |
| --- | ---: |
| /cinder/volume/manager.py | 53 |
| /cinder/db/sqlalchemy/api.py | 38 |
| /cinder/volume/flows/manager/create_volume.py | 28 |
| /cinder/db/api.py | 24 |
| /cinder/volume/drivers/lvm.py | 15 |

### Top 5 target classes
| Item | Count |
| --- | ---: |
| None | 71 |
| VolumeManager | 53 |
| CreateVolumeFromSpecTask | 26 |
| VolumeController | 16 |
| LVMVolumeDriver | 15 |

### Top 5 target functions
| Item | Count |
| --- | ---: |
| delete_volume | 24 |
| attach_volume | 14 |
| detach_volume | 13 |
| show | 13 |
| _get_volumes | 13 |

### Fault ↔ feature relationships
Top fault-type and component pairs (counts):
| Fault → Target | Count |
| --- | ---: |
| OPENSTACK_WRONG_RETURN_VALUE-VOLUME → /cinder/db/sqlalchemy/api.py | 32 |
| OPENSTACK_WRONG_RETURN_VALUE-VOLUME → /cinder/db/api.py | 22 |
| OPENSTACK_MISSING_PARAMETERS-VOLUME → /cinder/volume/manager.py | 13 |
| OPENSTACK_THROW_EXCEPTION-VOLUME → /cinder/volume/manager.py | 13 |
| OPENSTACK_MISSING_FUNCTION_CALL-VOLUME → /cinder/volume/manager.py | 13 |

Components experiencing the widest variety of fault types:
| Item | Count |
| --- | ---: |
| /cinder/volume/flows/manager/create_volume.py | 9 |
| /cinder/db/sqlalchemy/api.py | 7 |
| /cinder/image/image_utils.py | 7 |
| /cinder/volume/api.py | 6 |
| /cinder/volume/drivers/lvm.py | 6 |

## Neutron

* Total tests: **203**
* Unique target components: **26**
* Unique target classes: **32**
* Unique target functions: **76**

### Fault types
| Item | Count |
| --- | ---: |
| OPENSTACK_WRONG_RETURN_VALUE-NETWORK | 58 |
| OPENSTACK_THROW_EXCEPTION-NETWORK | 36 |
| OPENSTACK_MISSING_FUNCTION_CALL-NETWORK | 36 |
| OPENSTACK_MISSING_PARAMETERS-NETWORK | 36 |
| OPENSTACK_WRONG_PARAMETERS-NETWORK | 36 |
| OPENSTACK_WRONG_RETURN_VALUE-RPC | 1 |

### Top 5 target components
| Item | Count |
| --- | ---: |
| /neutron/plugins/ml2/plugin.py | 72 |
| /neutron/plugins/ml2/managers.py | 15 |
| /neutron/agent/dhcp/agent.py | 15 |
| /neutron/plugins/ml2/drivers/openvswitch/agent/ovs_neutron_agent.py | 13 |
| /neutron/agent/l3/router_info.py | 12 |

### Top 5 target classes
| Item | Count |
| --- | ---: |
| Ml2Plugin | 72 |
| TypeManager | 15 |
| SinkHole | 13 |
| RouterInfo | 12 |
| NeutronDbPluginV2 | 11 |

### Top 5 target functions
| Item | Count |
| --- | ---: |
| _create_network_db | 17 |
| _network_delete_after_delete_handler | 8 |
| _notify_mechanism_driver_for_segment_change | 8 |
| _process_internal_ports | 8 |
| create_network | 5 |

### Fault ↔ feature relationships
Top fault-type and component pairs (counts):
| Fault → Target | Count |
| --- | ---: |
| OPENSTACK_THROW_EXCEPTION-NETWORK → /neutron/plugins/ml2/plugin.py | 16 |
| OPENSTACK_MISSING_FUNCTION_CALL-NETWORK → /neutron/plugins/ml2/plugin.py | 16 |
| OPENSTACK_MISSING_PARAMETERS-NETWORK → /neutron/plugins/ml2/plugin.py | 16 |
| OPENSTACK_WRONG_PARAMETERS-NETWORK → /neutron/plugins/ml2/plugin.py | 16 |
| OPENSTACK_WRONG_RETURN_VALUE-NETWORK → /neutron/plugins/ml2/plugin.py | 8 |

Components experiencing the widest variety of fault types:
| Item | Count |
| --- | ---: |
| /neutron/plugins/ml2/managers.py | 5 |
| /neutron/plugins/ml2/plugin.py | 5 |
| /neutron/plugins/ml2/drivers/openvswitch/agent/ovs_neutron_agent.py | 5 |
| /neutron/db/ipam_backend_mixin.py | 5 |
| /neutron/db/agentschedulers_db.py | 5 |

## Nova

* Total tests: **439**
* Unique target components: **57**
* Unique target classes: **48**
* Unique target functions: **200**

### Fault types
| Item | Count |
| --- | ---: |
| OPENSTACK_WRONG_RETURN_VALUE-INSTANCE | 94 |
| OPENSTACK_MISSING_FUNCTION_CALL-INSTANCE | 66 |
| OPENSTACK_THROW_EXCEPTION-INSTANCE | 43 |
| OPENSTACK_MISSING_PARAMETERS-INSTANCE | 39 |
| OPENSTACK_WRONG_PARAMETERS-INSTANCE | 35 |
| OPENSTACK_WRONG_RETURN_VALUE-IMAGE | 27 |
| OPENSTACK_WRONG_RETURN_VALUE-VOLUME | 15 |
| OPENSTACK_MISSING_FUNCTION_CALL-VOLUME | 13 |
| OPENSTACK_WRONG_RETURN_VALUE-NETWORK | 13 |
| OPENSTACK_THROW_EXCEPTION-VOLUME | 11 |
| OPENSTACK_WRONG_PARAMETERS-VOLUME | 11 |
| OPENSTACK_MISSING_PARAMETERS-VOLUME | 10 |
| OPENSTACK_MISSING_FUNCTION_CALL-NETWORK | 7 |
| OPENSTACK_WRONG_PARAMETERS-NETWORK | 6 |
| URLLIB_MISSING_FUNCTION_CALL-CLEAR | 6 |
| OPENSTACK_WRONG_PARAMETERS-IMAGE | 6 |
| OPENSTACK_MISSING_FUNCTION_CALL-IMAGE | 5 |
| DISKIO_MISSING_FUNCTION_CALL-WRITE | 5 |
| OPENSTACK_THROW_EXCEPTION-NETWORK | 5 |
| OPENSTACK_MISSING_PARAMETERS-IMAGE | 4 |
| NETIO_MISSING_FUNCTION_CALL-CLOSE | 4 |
| OPENSTACK_THROW_EXCEPTION-IMAGE | 2 |
| OPENSTACK_MISSING_PARAMETERS-NETWORK | 2 |
| DISKIO_MISSING_FUNCTION_CALL-OPEN | 1 |
| OPENSTACK_WRONG_PARAMETERS-SSH | 1 |
| NETIO_MISSING_FUNCTION_CALL-SEND | 1 |
| OS_MISSING_FUNCTION_CALL-OS | 1 |
| OPENSTACK_MISSING_PARAMETERS-SSH | 1 |
| URLPARSE_MISSING_FUNCTION_CALL-URLSPLIT_IN_VAR | 1 |
| DISKIO_WRONG_PARAMETERS-WRITE | 1 |
| DISKIO_THROW_EXCEPTION-WRITE | 1 |
| DISKIO_MISSING_PARAMETERS-WRITE | 1 |
| OPENSTACK_THROW_EXCEPTION-SSH | 1 |

### Top 5 target components
| Item | Count |
| --- | ---: |
| /nova/compute/manager.py | 80 |
| /nova/virt/libvirt/driver.py | 51 |
| /nova/compute/api.py | 45 |
| /nova/db/sqlalchemy/api.py | 28 |
| /nova/compute/resource_tracker.py | 24 |

### Top 5 target classes
| Item | Count |
| --- | ---: |
| ComputeManager | 80 |
| API | 65 |
| LibvirtDriver | 51 |
| None | 43 |
| DeleteFromSelect | 28 |

### Top 5 target functions
| Item | Count |
| --- | ---: |
| _build_and_run_instance | 17 |
| schedule_and_build_instances | 14 |
| from_components | 10 |
| attach_volume | 9 |
| _attach_volume | 8 |

### Fault ↔ feature relationships
Top fault-type and component pairs (counts):
| Fault → Target | Count |
| --- | ---: |
| OPENSTACK_MISSING_FUNCTION_CALL-INSTANCE → /nova/compute/manager.py | 37 |
| OPENSTACK_WRONG_RETURN_VALUE-INSTANCE → /nova/db/sqlalchemy/api.py | 18 |
| OPENSTACK_THROW_EXCEPTION-INSTANCE → /nova/compute/manager.py | 13 |
| OPENSTACK_MISSING_PARAMETERS-INSTANCE → /nova/compute/manager.py | 11 |
| OPENSTACK_WRONG_RETURN_VALUE-INSTANCE → /nova/db/api.py | 11 |

Components experiencing the widest variety of fault types:
| Item | Count |
| --- | ---: |
| /nova/virt/libvirt/driver.py | 17 |
| /nova/compute/api.py | 16 |
| /nova/network/neutronv2/api.py | 11 |
| /nova/api/openstack/compute/servers.py | 10 |
| /nova/compute/manager.py | 9 |
