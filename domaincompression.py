import argparse
import dns.name

def domaincompression(domain_name):
  try:
    labels = domain_name.split('.')
    dns_name = dns.name.from_text(domain_name)
    dns_labels = []

    for label in labels:
      label_length_hex = format(len(label), '02x')
      dns_labels.extend([f"|{label_length_hex}|", label])

    # Join the DNS labels to form the DNS notation
    dns_notation = ''.join(dns_labels)
    return dns_notation

  except dns.name.BadLabelType:
    return "Invalid domain name format."

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Convert a domain name into DNS notation.")
  parser.add_argument("domain_name", help="Insert the domain name to convert.")
  args = parser.parse_args()
  result = domaincompression(args.domain_name)
  print(result)