using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Hiryu corpse" )]
	public class Hiryu : BaseMount
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.Dismount;
            } 
            
		[Constructable]
		public Hiryu() : this( "a Hiryu" )
		{
		}

		[Constructable]
		public Hiryu( string name ) : base( name, 243, 0x3E94, AIType.AI_Animal, FightMode.Agressor, 10, 1, 0.2, 0.4 )
		{
			BaseSoundID = 0x3F3;

			SetStr( 1200, 1400 );
			SetDex( 170, 270 );
			SetInt( 300, 325 );

			SetHits( 900, 1100 );
			SetStam(170,270);
			SetMana( 60, 65 );

			SetDamage( 125, 181 );

			SetDamageType( ResistanceType.Physical, 100 );

			SetResistance( ResistanceType.Physical, 55, 70 );
			SetResistance( ResistanceType.Fire, 70, 80 );
			SetResistance( ResistanceType.Cold, 15, 25 );
			SetResistance( ResistanceType.Poison, 40, 50 );
			SetResistance( ResistanceType.Energy, 40, 50 );

			SetSkill( SkillName.MagicResist, 85.0, 100.0 );
			SetSkill( SkillName.Tactics, 100.0, 110.0 );
			SetSkill( SkillName.Wrestling, 100.0, 120.0 );

			Fame = 2000;
			Karma = 2000;

			Tamable = true;
			ControlSlots = 4;
			MinTameSkill = 98.7;
			
		 PackGem(); 
         PackGem(); 
		 PackGem(); 
         PackGem();  
         PackGold( 1500, 1900 ); 
         PackMagicItems( 1, 5 ); 
			
			//pack bonzai seed
		}

		public override double GetControlChance( Mobile m )
		{
			return 1.0;
		}
		
		public override int TreasureMapLevel{ get{ return 3; } } 
		public override int Meat{ get{ return 16; } }
		public override int Hides{ get{ return 60; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Meat; } }

                public Hiryu( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}