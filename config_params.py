LLDP_CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <lldp xmlns="urn:ieee:std:802.1AB:yang:ieee802-dot1ab-lldp">
      <message-fast-tx>1</message-fast-tx>
      <message-tx-hold-multiplier>4</message-tx-hold-multiplier>
      <message-tx-interval>30</message-tx-interval>
      <reinit-delay>2</reinit-delay>
      <tx-credit-max>5</tx-credit-max>
      <tx-fast-init>4</tx-fast-init>
      <notification-interval>10</notification-interval>
      <port>
        <name>sw0p2</name>
        <dest-mac-address>00-60-65-8e-fd-43</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
      <port>
        <name>sw0p3</name>
        <dest-mac-address>00-60-65-8e-fd-44</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
      <port>
        <name>sw0p4</name>
        <dest-mac-address>00-60-65-8e-fd-45</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
      <port>
        <name>sw0p5</name>
        <dest-mac-address>00-60-65-8e-fd-46</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
      <port>
        <name>sw0p6</name>
        <dest-mac-address>00-60-65-8e-fd-47</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
      <port>
        <name>sw0ep</name>
        <dest-mac-address>00-60-65-8e-fd-42</dest-mac-address>
        <management-address-tx-port>
          <address-subtype xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:ipv6</address-subtype>
          <man-address>fe80::260:65ff:fe8e:fd42</man-address>
        </management-address-tx-port>
      </port>
  </lldp>
</config>
"""


BRIDGE_CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <bridges xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <bridge>
          <name>br0</name>
          <component>
          <name>br0</name>
          <filtering-database xc:operation="replace">
            <vlan-registration-entry>
              <database-id>1</database-id>
              <vids>1</vids>
              <port-map>
                <port-ref>1</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>2</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>3</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>4</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>5</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>6</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>untagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <entry-type>static</entry-type>
            </vlan-registration-entry>
            <vlan-registration-entry>
              <database-id>1</database-id>
              <vids>1100</vids>
              <port-map>
                <port-ref>2</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>tagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>3</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>tagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>4</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>tagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <port-map>
                <port-ref>5</port-ref>
                <static-vlan-registration-entries>
                  <registrar-admin-control>normal</registrar-admin-control>
                  <vlan-transmitted>tagged</vlan-transmitted>
                </static-vlan-registration-entries>
              </port-map>
              <entry-type>static</entry-type>
            </vlan-registration-entry>
          </filtering-database>
          </component>
        </bridge>
    </bridges>
</config>
"""


BRIDGE_FILTER = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <bridges xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge">
      <bridge>
        <name>br0</name>
      </bridge>
  </bridges>
</filter>
"""

LLDP_FILTER = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <lldp>
  </lldp>
</filter>
"""


QBV_CONFIG = f"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interface>
      <name>sw0p1</name>
      <bridge-port xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <component-name>br0</component-name>
      <pvid>1</pvid>
      <default-priority>1</default-priority>
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
      </bridge-port>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <gate-enabled>true</gate-enabled>
        <admin-gate-states>255</admin-gate-states>
        <admin-control-list-length>2</admin-control-list-length>
        <admin-control-list>
          <index>0</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>255</gate-states-value>
          <time-interval-value>200000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-control-list>
          <index>1</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>2</gate-states-value>
          <time-interval-value>600000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-cycle-time>
          <numerator>1</numerator>
          <denominator>800</denominator>
        </admin-cycle-time>
        <admin-cycle-time-extension>0</admin-cycle-time-extension>
        <admin-base-time>
          <seconds>0</seconds>
          <fractional-seconds>0</fractional-seconds>
        </admin-base-time>
        <config-change>true</config-change>
      </gate-parameters>
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
      </bridge-port>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <gate-enabled>true</gate-enabled>
        <admin-gate-states>255</admin-gate-states>
        <admin-control-list-length>2</admin-control-list-length>
        <admin-control-list>
          <index>0</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>255</gate-states-value>
          <time-interval-value>200000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-control-list>
          <index>1</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>2</gate-states-value>
          <time-interval-value>600000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-cycle-time>
          <numerator>1</numerator>
          <denominator>800</denominator>
        </admin-cycle-time>
        <admin-cycle-time-extension>0</admin-cycle-time-extension>
        <admin-base-time>
          <seconds>0</seconds>
          <fractional-seconds>0</fractional-seconds>
        </admin-base-time>
        <config-change>true</config-change>
      </gate-parameters>
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
      <default-priority>7</default-priority>
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
      </bridge-port>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
      <gate-enabled>true</gate-enabled>
      <admin-gate-states>255</admin-gate-states>
      <admin-control-list-length>2</admin-control-list-length>
      <admin-control-list>
        <index>0</index>
        <operation-name>set-gate-states</operation-name>
        <sgs-params>
        <gate-states-value>255</gate-states-value>
        <time-interval-value>200000</time-interval-value>
        </sgs-params>
      </admin-control-list>
      <admin-control-list>
        <index>1</index>
        <operation-name>set-gate-states</operation-name>
        <sgs-params>
        <gate-states-value>2</gate-states-value>
        <time-interval-value>600000</time-interval-value>
        </sgs-params>
      </admin-control-list>
      <admin-cycle-time>
        <numerator>1</numerator>
        <denominator>800</denominator>
      </admin-cycle-time>
      <admin-cycle-time-extension>0</admin-cycle-time-extension>
      <admin-base-time>
        <seconds>0</seconds>
        <fractional-seconds>0</fractional-seconds>
      </admin-base-time>
      <config-change>true</config-change>
      </gate-parameters>
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
      </bridge-port>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xc:operation="replace">
        <gate-enabled>true</gate-enabled>
        <admin-gate-states>255</admin-gate-states>
        <admin-control-list-length>2</admin-control-list-length>
        <admin-control-list>
          <index>0</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>255</gate-states-value>
          <time-interval-value>200000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-control-list>
          <index>1</index>
          <operation-name>set-gate-states</operation-name>
          <sgs-params>
          <gate-states-value>2</gate-states-value>
          <time-interval-value>600000</time-interval-value>
          </sgs-params>
        </admin-control-list>
        <admin-cycle-time>
          <numerator>1</numerator>
          <denominator>800</denominator>
        </admin-cycle-time>
        <admin-cycle-time-extension>0</admin-cycle-time-extension>
        <admin-base-time>
          <seconds>0</seconds>
          <fractional-seconds>0</fractional-seconds>
        </admin-base-time>
        <config-change>true</config-change>
      </gate-parameters>
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


def get_interface_filter(interface: str):
    return f"""
          <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
              <interface>
                <name>{interface}</name>
              </interface>
            </interfaces>
          </filter>
          """


INTERFACE_FILTER = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>sw0p2</name>
    </interface>
  </interfaces>
</filter>
"""


OPERATION = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interface>
      <name>sw0p1</name>
    </interface>
    <interface>
      <name>sw0p2</name>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <config-change>false</config-change>
      </gate-parameters>
    </interface>
    <interface>
      <name>sw0p3</name>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <config-change>false</config-change>
      </gate-parameters>
    </interface>
    <interface>
      <name>sw0p4</name>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <config-change>false</config-change>
      </gate-parameters>
    </interface>
    <interface>
      <name>sw0p5</name>
      <gate-parameters xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <config-change>false</config-change>
      </gate-parameters>
    </interface>
    <interface>
      <name>sw0p6</name>
    </interface>
  </interfaces>
</config>
"""
