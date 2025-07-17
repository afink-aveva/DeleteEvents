# DeleteEvents

Sample script to delete all Events for a specified EventTypeId.  The EventType can optionally also be deleted.

## Usage
- Requires Python 3.7+
- Install dependencies `pip install -f requirements.txt`
- Update `appsettings.json` accordingly, note you will need a [Client-Credentials Client Id and Secret](https://docs.aveva.com/bundle/connect-data-services/page/1263324.html) 
- Specify the `EventTypeId` and optionally `DeleteEventType` on lines 5 and 6 of `Program.py`
- Run the script with `python Program.py`

**Please Note**: These code samples are not part of a supported product release. While they demonstrate the use of our APIs and technology, they come as-is without the following features or guarantees associated with official product releases:

What’s Not Included:

1. **Official Support**
* No guaranteed technical support or issue resolution.
* No support via customer service channels.
2. **Quality Assurance**
* No extensive testing for stability, scalability, or security.
* May contain bugs or limitations that have not been addressed.
3. **Updates or Maintenance**
* No regular updates to align with API changes or new product releases.
* Potential for deprecation without notice.
4. **Documentation Completeness**
* May not include comprehensive guides, installation instructions, or troubleshooting steps.
5. **Warranties or Guarantees**
* No guarantees of performance, compatibility, or reliability.
6. **Integration Readiness**
* Not designed for seamless integration into production environments.
7. **Compliance and Certification**
* No guarantees of compliance with regulatory or industry standards.

**Intended Use**:
These code samples are provided for educational purposes and as a reference for learning and experimentation. Developers are encouraged to modify and extend the code to suit their specific use cases. For production applications, we recommend consulting our official documentation and leveraging supported SDKs, APIs, and tools.
We welcome your feedback and contributions, but please understand that this repository is not actively monitored for support requests.