from pydantic import BaseModel
from typing import List

HIGH_PRIORITY_INGRESS_PCP = 6

PORT_PARAM = """
        <priority-regeneration>
            <priority0>0</priority0>
            <priority1>1</priority1>
            <priority2>2</priority2>
            <priority3>3</priority3>
            <priority4>4</priority4>
            <priority5>5</priority5>
            <priority6>6</priority6>
            <priority7>7</priority7>
        </priority-regeneration>
        <service-access-priority>
            <priority0>0</priority0>
            <priority1>1</priority1>
            <priority2>2</priority2>
            <priority3>3</priority3>
            <priority4>4</priority4>
            <priority5>5</priority5>
            <priority6>6</priority6>
            <priority7>7</priority7>
            </service-access-priority>
        <traffic-class>
            <priority0>1</priority0>
            <priority1>0</priority1>
            <priority2>2</priority2>
            <priority3>3</priority3>
            <priority4>4</priority4>
            <priority5>5</priority5>
            <priority6>6</priority6>
            <priority7>7</priority7>
        </traffic-class>
        <acceptable-frame>admit-all-frames</acceptable-frame>
"""


class ControlListEntry(BaseModel):
    bitmask: int
    value: int


def create_control_list_entries(control_list: List[ControlListEntry]):
    entries = ""
    for index, entry in enumerate(control_list):
        entries += f"""
        <admin-control-list>
            <index>{index}</index>
            <operation-name>set-gate-states</operation-name>
            <sgs-params>
            <gate-states-value>{entry.bitmask}</gate-states-value>
            <time-interval-value>{entry.value}</time-interval-value>
            </sgs-params>
        </admin-control-list>
    """

    return entries


def create_qbv_gate_entry(control_list: List[ControlListEntry], cycle_time, off_set=0):
    qbv_gate = f"""
    <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <gate-enabled>true</gate-enabled>
        <admin-gate-states>255</admin-gate-states>
        <admin-control-list-length>{len(control_list)}</admin-control-list-length>

        {create_control_list_entries(control_list)}

        <admin-cycle-time>
          <numerator>1</numerator>
          <denominator>{cycle_time}</denominator>
        </admin-cycle-time>
        <admin-cycle-time-extension>0</admin-cycle-time-extension>
        <admin-base-time>
          <seconds>0</seconds>
          <fractional-seconds>{off_set}</fractional-seconds>
        </admin-base-time>
        <config-change>{"true" if len(control_list) else "false"}</config-change>
    </gate-parameters>
    """

    return qbv_gate


def _get_ctrl_list(bm1, v1, bm2, v2) -> List[ControlListEntry]:
    control_list = [
        ControlListEntry(bitmask=bm1, value=v1),
        ControlListEntry(bitmask=bm2, value=v2),
    ]
    return control_list


def get_qbv_config(cycle_time=800, off_set=0):
    QBV_CONFIG = f"""
  <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <interface>
        <name>sw0p1</name>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <component-name>br0</component-name>
        <pvid>1</pvid>
        <default-priority>1</default-priority>
        {PORT_PARAM}
        </bridge-port>
      </interface>
      <interface>
        <name>sw0p2</name>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>0</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>1</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>2</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>3</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>4</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>5</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>6</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>7</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <component-name>br0</component-name>
          <pvid>1</pvid>
          <default-priority>1</default-priority>
          {PORT_PARAM}
        </bridge-port>
        {create_qbv_gate_entry(_get_ctrl_list(255, 200000, 64, 600000), cycle_time)}
        <ethernet xmlns="urn:ieee:std:802.3:yang:ieee802-ethernet-interface" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
          <auto-negotiation>
            <enable>true</enable>
          </auto-negotiation>
        </ethernet>
      </interface>

      <interface>
        <name>sw0p3</name>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>0</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>1</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>2</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>3</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>4</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>5</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>6</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>7</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <component-name>br0</component-name>
          <pvid>1</pvid>
          <default-priority>1</default-priority>
          {PORT_PARAM}
        </bridge-port>
        {create_qbv_gate_entry(_get_ctrl_list(255, 200000, 64, 600000), 800)}
        <ethernet xmlns="urn:ieee:std:802.3:yang:ieee802-ethernet-interface" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
          <auto-negotiation>
            <enable>true</enable>
          </auto-negotiation>
        </ethernet>
      </interface>

      <interface>
        <name>sw0p4</name>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>0</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>1</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>2</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>3</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>4</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>5</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>6</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>7</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <component-name>br0</component-name>
          <pvid>1</pvid>
          <default-priority>{HIGH_PRIORITY_INGRESS_PCP}</default-priority>
          {PORT_PARAM}
        </bridge-port>
        {create_qbv_gate_entry([], 800)}
        <ethernet xmlns="urn:ieee:std:802.3:yang:ieee802-ethernet-interface" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <auto-negotiation>
          <enable>true</enable>
        </auto-negotiation>
        </ethernet>
      </interface>

      <interface>
        <name>sw0p5</name>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>0</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>1</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>2</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>3</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>4</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <traffic-class>5</traffic-class>
        <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>6</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <max-sdu-table xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <traffic-class>7</traffic-class>
          <queue-max-sdu>1504</queue-max-sdu>
        </max-sdu-table>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <component-name>br0</component-name>
          <pvid>1</pvid>
          <default-priority>1</default-priority>
          {PORT_PARAM}
        </bridge-port>
        {create_qbv_gate_entry(_get_ctrl_list(255, 200000, 64, 600000), 800)}
        <ethernet xmlns="urn:ieee:std:802.3:yang:ieee802-ethernet-interface" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <auto-negotiation>
          <enable>true</enable>
        </auto-negotiation>
        </ethernet>
      </interface>

      <interface>
        <name>sw0p6</name>
        <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <component-name>br0</component-name>
          <pvid>1</pvid>
          <default-priority>1</default-priority>
          {PORT_PARAM}
        </bridge-port>
        <ethernet xmlns="urn:ieee:std:802.3:yang:ieee802-ethernet-interface" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <auto-negotiation>
          <enable>true</enable>
        </auto-negotiation>
        </ethernet>
      </interface>
    </interfaces>
  </config>
  """

    return QBV_CONFIG
