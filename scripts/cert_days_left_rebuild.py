import sys
import socket
import ssl
import tempfile
import datetime as dt
import os
def main():
   if len(sys.argv)!=2:
    print("Usage: python scripts/cert_days_left.py example.com")
    return 2
   
   hostname=sys.argv[1]
   sock=socket.create_connection((hostname,443),timeout=5)
  
   context=ssl._create_unverified_context()
   tls_sock=context.wrap_socket(sock,server_hostname=hostname)

   cert_bytes=tls_sock.getpeercert(binary_form=True)
  
   cert_pem=ssl.DER_cert_to_PEM_cert(cert_bytes)
   
   temp_file = tempfile.NamedTemporaryFile("w", delete=False, suffix=".pem")
   temp_file.write(cert_pem)
   temp_path = temp_file.name
   temp_file.close()

  
   cert_info=ssl._ssl._test_decode_cert(temp_path)
   os.remove(temp_path)
   not_after=cert_info["notAfter"]
   
   expiry=dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
  
   now=dt.datetime.now()
   delta=expiry-now
   day_left=delta.days
   print(f"OK {hostname} certificate expires in {day_left} days")




if __name__ == "__main__":
    main()
